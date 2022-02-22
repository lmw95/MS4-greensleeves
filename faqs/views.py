from django.shortcuts import render


def faqs(request):
    """Renders the FAQs page"""
    return render(request, 'faqs/faqs.html')
