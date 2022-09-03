from django.contrib import admin
from django.urls import path

from .models import Phone
from .views import show_catalog, show_product

urlpatterns = [
    path("", show_catalog, name='catalog'),
    path('<slug:slug>/', show_product, name='phone')
]