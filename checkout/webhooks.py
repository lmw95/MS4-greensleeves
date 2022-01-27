from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from checkout.webhook_handler import StripeWH_Handler
import stripe


@require_POST
@csrf_exempt
def webhook(request):
    """Listens for webhooks from Stripe"""

    #Setup
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api.key = settings.STRIPE_SECRET_KEY

    # Get the data and verify its signature
    payload = request.body
    sig_handler = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_hander, wh_secret
        )
    except ValueError as e:
        return HttpResponse(status=200)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)
    except Exception as e:
        return HttpResponse(content=e, status=400)

    print('success')
    return HttpResponse(status=200)