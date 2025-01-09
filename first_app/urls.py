from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('shop/', views.shop, name='shop'),
    path('contact/', views.contact, name='contact'),
    path('product_details/<int:product_id>/', views.product_details, name='product_details')
]