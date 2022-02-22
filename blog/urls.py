from django.urls import path
from . import views
from blog.views import blog_page


urlpatterns = [
    path('', views.blog, name='blog'),
    path('<slug:slug>', views.blog_page, name='blog_page'),
]
