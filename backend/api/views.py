
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Recette, Order,Profile
from .serializers import RecetteSerializer, OrderSerializer, ProfileSerializer

class RecetteAPIView(APIView):
    def get(self, request):
        # Logique pour récupérer toutes les recettes
        toutes_les_recettes = Recette.objects.all()
        serializer = RecetteSerializer(toutes_les_recettes, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Logique pour ajouter une nouvelle recette
        serializer = RecetteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class OrderAPIView(APIView):
    # recuperer toutes les commandes
    def get(self, request):
        toutes_les_commandes = Order.objects.all()
        serializer = OrderSerializer(toutes_les_commandes, many=True)
        return Response(serializer.data)

    # ajouter une nouvelle commandes
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # modifier une commande
    def put(self, request, id):
        try:
            # Récupérer la commande à partir de son ID
            modify = Order.objects.get(id=id)
        except Order.DoesNotExist:
            # Retourner une réponse 404 si la commande n'existe pas
            return Response({"error": "Commande introuvable"}, status=status.HTTP_404_NOT_FOUND)

        # Mettre à jour la commande avec les données envoyées dans la requête
        serializer = OrderSerializer(instance=modify, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        # Retourner les erreurs si les données ne sont pas valides
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    # supprimer une commande
    def delete(self, request, *args, **kwargs):
        try:
            # Récupérer le profil à partir de l'ID (kwargs['id'])
            order_id = kwargs.get('id')  # Extraction depuis les arguments
            order = Order.objects.get(id=order_id)
            order.delete()
            return Response({"message": "Profil supprimé avec succès"}, status=status.HTTP_200_OK)
        except Order.DoesNotExist:
            return Response({"error": "Profil introuvable"}, status=status.HTTP_404_NOT_FOUND)

# recuperer la liste des accounts
class ProfileAPIView(APIView):

    # recuperer tous les accounts
    def get(self, request):
        toutes_les_comptes = Profile.objects.all()
        serializer = ProfileSerializer(toutes_les_comptes, many=True)
        return Response(serializer.data)
    
    # ajouter un nouveau compte
    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # modifier un compte existant
    def put(self, request, id):

        try:
            # Récupérer la commande à partir de son ID
            modify = Profile.objects.get(id=id)
        except Profile.DoesNotExist:
            # Retourner une réponse 404 si la commande n'existe pas
            return Response({"error": "Compte  introuvable"}, status=status.HTTP_404_NOT_FOUND)

        # Mettre à jour la commande avec les données envoyées dans la requête
        serializer = ProfileSerializer(instance=modify, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        # Retourner les erreurs si les données ne sont pas valides
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # supprimer un compte existant
    def delete(self, request, *args, **kwargs):
        try:
            # Récupérer le profil à partir de l'ID (kwargs['id'])
            profile_id = kwargs.get('id')  # Extraction depuis les arguments
            profile = Profile.objects.get(id=profile_id)
            profile.delete()
            return Response({"message": "Profil supprimé avec succès"}, status=status.HTTP_200_OK)
        except Profile.DoesNotExist:
            return Response({"error": "Profil introuvable"}, status=status.HTTP_404_NOT_FOUND)
