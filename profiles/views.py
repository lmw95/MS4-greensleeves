from django.shortcuts import render

# Create your views here.
def profile():
    """Displays user's profile"""
    context = {}
    
    return render(request, 'profiles/profile.html', context)
