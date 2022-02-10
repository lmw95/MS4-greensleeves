from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order

# Create your views here.
def profile(request):
    """Displays user's profile"""

    profile = get_object_or_404(UserProfile, user=request.user)
    phone = profile.default_phone_number
    line1 = profile.default_street_address1
    line2 = profile.default_street_address2
    town = profile.default_town_or_city
    postcode = profile.default_postcode
    country = profile.default_country

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed, please make sure form is valid')

    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    context = {
        'profile': profile,
        'form': form,
        'orders': orders,
        'phone_number': phone,
        'line1': line1,
        'line2': line2,
        'town': town,
        'postcode': postcode,
        'country': country,
    }
    
    return render(request, 'profiles/profile.html', context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}.'
        'A cofirmation email was sent on the order date.'
        ))

    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, 'checkout/checkout_success.html', context)