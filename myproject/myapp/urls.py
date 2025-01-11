from django.urls import path
from .views import ItemList, frontend

urlpatterns = [
    path('items/', ItemList.as_view(), name='item-list'),
    path('',frontend, name='frontend'),
]
