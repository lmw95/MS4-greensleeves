from django.http import HttpResponse

class StripeWH_Handler:
    """Handles Stripe webhooks"""

    def __init__(self, request):
        self.request = request


    def handle_event(self, event):
        """Handles a generic/unknown/unexpected webhook event"""
        return HttpResponse(
            content=f'Unhandled webhook recieved: {event["type"]}',
            status=200)


    def handle_payment_intent_succeeded(self, event):
        """Handles the payment_intent.succeed webhook from Stipe"""
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200)
    

    def handle_payment_intent_payment_failed(self, event):
        """Handles the payment_intent.succeed webhook from Stripe"""
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200)

