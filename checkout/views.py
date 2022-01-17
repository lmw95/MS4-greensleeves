from django.shortcuts import render, redirect, reverse
from django.contrib import messages

# Create your views here.
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'There is nothing in your bag right now')
        return redirect(reverse('shop'))

    return render(request, 'checkout/checkout.html')
