from django.contrib import admin
from django.urls import path,include

from .views import  HomeView,checkout,ItemDetailView,add_to_cart,remove_from_cart,OrderSummeryView

app_name ='core'

urlpatterns = [
    path('',  HomeView.as_view(),name='home-list'),
    path('order-summery/',OrderSummeryView.as_view(),name='order-summery'),
    path('checkout/',checkout,name='checkout'),
     path('product/<slug>/',ItemDetailView.as_view(),name='product'),
     path('add-to-cart/<slug>/',add_to_cart,name='add-to-cart'),
     path('remove-from-cart/<slug>/',remove_from_cart,name='remove-from-cart')
]