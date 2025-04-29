
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Recette
from .serializers import RecetteSerializer

class RecetteAPIView(APIView):
    def get(self, request):
        # Logique pour récupérer toutes les recettes
        recettes = Recette.objects.all()
        serializer = RecetteSerializer(recettes, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Logique pour ajouter une nouvelle recette
        serializer = RecetteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

