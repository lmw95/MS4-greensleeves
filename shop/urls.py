from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.shop, name='shop'),
    path('<product_id>', views.item_page, name='item_page'),
]