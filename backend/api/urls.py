from django.contrib import admin

from django.urls import path
from .views import RecetteAPIView,OrderAPIView,ProfileAPIView

urlpatterns = [
    # Routes pour Recette
    path('recettes/', RecetteAPIView.as_view(), name='recettes'),

    # Routes pour Order
    path('orders/', OrderAPIView.as_view(), name='orders-list'),
    path('orders/<int:id>/', OrderAPIView.as_view(), name='orders-detail'),

    # Routes pour Profile
    path('profiles/', ProfileAPIView.as_view(), name='profile-list'),
    path('profiles/<int:id>/', ProfileAPIView.as_view(), name='profile-detail'),
]

