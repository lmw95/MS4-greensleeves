from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe

# Create your views here.
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'There is nothing in your bag right now')
        return redirect(reverse('shop'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KJGRPDIv1wyBqdW62WTpYQH32KS1dEjgRJtHpI7oczuqNRD9fd22RPqhLuC5CAmOjxrT0hEUtqYFsJ5eRpbk4fk00Km6zGuWO',
        'client_secret': 'test',
    }

    return render(request, 'checkout/checkout.html', context)
