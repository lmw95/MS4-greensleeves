from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'There is nothing in your bag right now')
        return redirect(reverse('shop'))

    order_form = OrderForm()
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KJGRPDIv1wyBqdW62WTpYQH32KS1dEjgRJtHpI7oczuqNRD9fd22RPqhLuC5CAmOjxrT0hEUtqYFsJ5eRpbk4fk00Km6zGuWO',
        'client_secret': 'test',
    }

    return render(request, 'checkout/checkout.html', context)
