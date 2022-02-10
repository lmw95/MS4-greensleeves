from django.urls import path
from . import views


urlpatterns = [
    path('', views.shop, name='shop'),
    path('<int:product_id>/', views.item_page, name='item_page'),
    path('add/', views.add_item, name='add_item'),
    path('edit/<int:product_id>/', views.edit_item, name='edit_item'),
    path('delete/<int:product_id>/', views.delete_item, name='delete_item'),
]
