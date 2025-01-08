from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Acceuil'),
    path('about/', views.about, name='A propos'),
    path('blog/', views.blog, name='Blog'),
    path('shop/', views.shop, name='Shop'),
    path('contact/', views.contact, name='Contact')
]