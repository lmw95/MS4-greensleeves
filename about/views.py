from django.shortcuts import render


def about_us(request):
    """Renders the 'About us' page"""
    return render(request, 'about/about-us.html')
