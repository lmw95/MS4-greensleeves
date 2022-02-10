from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.shop, name='shop'),
    path('<int:product_id>', views.item_page, name='item_page'),
    path('add/', views.add_item, name='add_item'),
]