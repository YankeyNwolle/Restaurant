from django.contrib import admin
from django.urls import path, include
from . import views

from django.urls import path
from .views import RecetteAPIView

urlpatterns = [
    path('recettes/', RecetteAPIView.as_view(), name='recettes'),
]

