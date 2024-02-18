# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('ordered_products/', views.ordered_products, name='ordered_products'),
]
