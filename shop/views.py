from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.
def shop(request):
    """A view to return main shop page with all items, including sorting and search queries"""

    products = Product.objects.all()
    query = None
    categories = None
    seasonal_collection = None

    if request.GET:
        if 'seasonal_collection' in request.GET:
            seasonal_collection = request.GET['seasonal_collection'].split(',')
            products = products.filter(seasonal_collection__in=seasonal_collection)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Oops, you haven't searched for anything!")
                return redirect(reverse('shop'))
            
            queries = Q(name__icontains=query) | Q(
                item_description__icontains=query) | Q(
                seasonal_collection__icontains=query) | Q(
                top_tip__icontains=query) | Q(
                water_need__icontains=query) | Q(
                humidity_need__icontains=query) | Q(
                growth_need__icontains=query) | Q(
                temp_need__icontains=query) | Q(
                light_need__icontains=query) | Q(
                ease_of_care__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'shop/shop.html', context)


def item_page(request, product_id):
    """A view to return item page with product information"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product
    }

    return render(request, 'shop/item-page.html', context)
