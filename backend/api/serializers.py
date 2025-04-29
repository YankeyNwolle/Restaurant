from rest_framework import serializers
from django.contrib.auth.models import User  
from .models import Profile, Recette, Ingredient, Etape


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["phone", "email"]

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ["id", "username", "profile"]

class RecetteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recette
        fields = '__all__'  

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class EtapeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etape
        fields = '__all__'
