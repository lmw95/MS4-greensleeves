from django.shortcuts import render
from .models import Product

# Create your views here.
def shop(request):
    """A view to return main shop page"""

    products = Product.objects.all

    context = {
        'products': products
    }

    return render(request, 'shop/shop.html')