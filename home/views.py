from django.shortcuts import render, get_object_or_404
import datetime
from datetime import date
from shop.models import Product

# Create your views here.
def index(request):
    """A view to return index page
        Renders the relevant seasonal collection according to current date"""

    current_date = datetime.date.today()

    collection_active = ""
    emotion = ""

    # Collection dates to display in front page
    w_start = date(2021, 10, 1)
    w_end = date(2022, 2, 1)
    winter_collection = w_end - w_start

    val_start = date(2022, 2, 1)
    val_end = date(2022, 2, 14)
    valentines_collection = val_end - val_start

    spr_start = date(2022, 2, 15)
    spr_end = date(2022, 5, 31)
    spring_collection = spr_end - spr_start

    sum_start = date(2022, 6, 1)
    sum_end = date(2022, 8, 31)
    summer_collection = sum_end - sum_start

    if w_start <= current_date <= w_end:
        collection_active = "winter"
        emotion = "ready for festive fun"
    elif spr_start <= current_date <= spr_end:
        collection_active = "spring"
        emotion = "set for a fresh start"
    elif sum_start <= current_date <= sum_end:
        collection_active = "summer"
        emotion = "refreshingly vibrant"
    else:
        collection_active = "valentines"
        emotion = "like falling in love"

    seasonal_items = Product.objects.filter(seasonal_collection=collection_active)

    context = {
         'collection_active': collection_active,
         'winter_collection': winter_collection,
         'valentines_collection': valentines_collection,
         'spring_collection': spring_collection,
         'summer_collection': summer_collection,
         'emotion': emotion,
         'seasonal_items': seasonal_items,
    }

    return render(request, 'home/index.html', context)
