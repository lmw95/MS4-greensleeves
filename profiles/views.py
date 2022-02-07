from django.shortcuts import render

# Create your views here.
def profile(request):
    """Displays user's profile"""
    context = {}
    
    return render(request, 'profiles/profile.html', context)
