# urls.py
from django.urls import path
from .views import mpesa_callback

urlpatterns = [
    path('', mpesa_callback, name='mpesa_callback'),
]
