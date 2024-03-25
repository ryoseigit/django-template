from django.urls import path
from .views import get_mainapp

urlpatterns = [
    path('', get_mainapp)
]