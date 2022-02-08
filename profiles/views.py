from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm

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
