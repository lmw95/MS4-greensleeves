from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from shop.models import Product


# Create your views here.
def view_bag(request):
    """Renders shopping bag"""
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """Add quantity of specified item to shopping bag"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'Updated {product.friendly_name} to {bag[item_id]}x')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.friendly_name} to bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def update_bag(request, item_id):
    """Updates quantity of items in shopping bag"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'Updated {product.friendly_name} to {bag[item_id]}x')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {product.friendly_name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Removes item from shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        messages.success(request, f'Removed {product.friendly_name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
