from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, OrderLineItem
from shop.models import Product
from profiles.models import UserProfile

import json
import time


class StripeWH_Handler:
    """Handles Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send user a confirmation email of order"""
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email],
        )

    def handle_event(self, event):
        """Handles a generic/unknown/unexpected webhook event"""
        return HttpResponse(
            content=f'Unhandled webhook recieved: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """Handles the payment_intent.succeed webhook from Stipe"""
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.data.charges[0].amount/100, 2)

        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        profile = None
        username = intent.metadata.username
        if user != 'AnonymousUser':
            profile = UserProfile.objects.get(user_username=username)
            if save_info():
                profile.default_phone_number__iexact=shipping_details.phone,
                profile.default_street_address1__iexact=shipping_details.address.line1
                profile.default_street_address2__iexact=shipping_details.address.line2
                profile.default_town_or_city__iexact=shipping_details.address.city
                profile.default_postcode__iexact=shipping_details.address.postal_code
                profile.default_country__iexact=shipping_details.address.country
                profile.save()

        order_exists = False
        attempt = 1
        while attempt <=5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    town_or_city__iexact=shipping_details.address.city,
                    postcode__iexact=shipping_details.address.postal_code,
                    country__iexact=shipping_details.address.country,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                    content=f'Webhook recieved: {event["type"]} | Success: verified order already in database',
                    status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    town_or_city=shipping_details.address.city,
                    postcode=shipping_details.address.postal_code,
                    country=shipping_details.address.country,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(bag).items():
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                    order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook recieved: {event["type"]} | ERROR: {e}',
                    status=500)
        self._send_confirmation_email(order)
        return HttpResponse(
                content=f'Webhook recieved: {event["type"]} | SUCCESS: Created order in webhook',
                status=200)
    

    def handle_payment_intent_payment_failed(self, event):
        """Handles the payment_intent.payment_failed webhook from Stripe"""
        return HttpResponse(
            content=f'Payment failed webhook recieved: {event["type"]}',
            status=200)
