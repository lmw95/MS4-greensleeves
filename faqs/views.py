from django.shortcuts import render

# Create your views here.

def faqs(request):
    """Renders the FAQs page"""
    return render(request, 'faqs/faqs.html')
