from django.urls import path
from . import views

urlpatterns = [
    path('', views.AppleStore, name='AppleStore'),
    path('iPhone/', views.iPhones, name='iPhone'),
    path('iPhone/iPhoneDetails/<int:iPhone_id>/', views.iPhoneDetails, name='iPhoneDetails'),
    path('iPhone/shop/', views.iPhoneShop, name='iPhoneShop'),
]