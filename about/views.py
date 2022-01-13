from django.shortcuts import render

# Create your views here.
def about_us(request):
    """Renders the 'About us' page"""
    return render(request, 'about/about-us.html')