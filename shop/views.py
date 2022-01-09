from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category

# Create your views here.
def shop(request):
    """A view to return main shop page with all items, including sorting and search queries"""

    products = Product.objects.all()
    query = None
    categories = None
    seasonal_collection = None
    water_need = None
    light_need = None
    temp_need = None
    humidity_need = None
    growth_need = None
    ease_of_care = None
    sort = None
    direction = None

    if request.GET:
        if 'seasonal_collection' in request.GET:
            seasonal_collection = request.GET['seasonal_collection'].split(',')
            products = products.filter(seasonal_collection__in=seasonal_collection)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'water_need' in request.GET:
            water_need = request.GET['water_need'].split(',')
            products = products.filter(water_need__in=water_need)

        if 'light_need' in request.GET:
            light_need = request.GET['light_need'].split(',')
            products = products.filter(light_need__in=light_need)

        if 'temp_need' in request.GET:
            temp_need = request.GET['temp_need'].split(',')
            products = products.filter(temp_need__in=temp_need)

        if 'humidity_need' in request.GET:
            humidity_need = request.GET['humidity_need'].split(',')
            products = products.filter(humidity_need__in=humidity_need)

        if 'growth_need' in request.GET:
            growth_need = request.GET['growth_need'].split(',')
            products = products.filter(growth_need__in=growth_need)

        if 'ease_of_care' in request.GET:
            ease_of_care = request.GET['ease_of_care'].split(',')
            products = products.filter(ease_of_care__in=ease_of_care)

        if request.GET:
            if 'sort' in request.GET:
                sortkey = request.GET['sort']
                sort = sortkey
                if sortkey == 'name':
                    sortkey = 'lower_name'
                    products = products.annotate(lower_name=Lower('name'))

                if 'direction' in request.GET:
                    direction = request.GET['direction']
                    if direction == 'desc':
                        sortkey = f'-{sortkey}'
                products = products.order_by(sortkey)

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

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_seasonal': seasonal_collection,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'shop/shop.html', context)


def item_page(request, product_id):
    """A view to return item page with product information"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product
    }

    return render(request, 'shop/item-page.html', context)
