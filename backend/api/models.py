from django.db import models
from django.contrib.auth.models import User  
import datetime
from django.utils import timezone


# models pour les recettes

class Recette(models.Model):
    PAYS_AFRIQUE = [
        ('ALG', 'Algérie'),
        ('ANG', 'Angola'),
        ('BEN', 'Bénin'),
        ('BOT', 'Botswana'),
        ('BFA', 'Burkina Faso'),
        ('BDI', 'Burundi'),
        ('CPV', 'Cap-Vert'),
        ('CMR', 'Cameroun'),
        ('CAF', 'République Centrafricaine'),
        ('TCD', 'Tchad'),
        ('COM', 'Comores'),
        ('COG', 'Congo'),
        ('COD', 'République Démocratique du Congo'),
        ('DJI', 'Djibouti'),
        ('EGY', 'Égypte'),
        ('GNQ', 'Guinée Équatoriale'),
        ('ERI', 'Érythrée'),
        ('SWZ', 'Eswatini'),
        ('ETH', 'Éthiopie'),
        ('GAB', 'Gabon'),
        ('GMB', 'Gambie'),
        ('GHA', 'Ghana'),
        ('GIN', 'Guinée'),
        ('GNB', 'Guinée-Bissau'),
        ('CIV', 'Côte d’Ivoire'),
        ('KEN', 'Kenya'),
        ('LSO', 'Lesotho'),
        ('LBR', 'Libéria'),
        ('LBY', 'Libye'),
        ('MDG', 'Madagascar'),
        ('MWI', 'Malawi'),
        ('MLI', 'Mali'),
        ('MRT', 'Mauritanie'),
        ('MUS', 'Maurice'),
        ('MAR', 'Maroc'),
        ('MOZ', 'Mozambique'),
        ('NAM', 'Namibie'),
        ('NER', 'Niger'),
        ('NGA', 'Nigéria'),
        ('RWA', 'Rwanda'),
        ('STP', 'Sao Tomé-et-Principe'),
        ('SEN', 'Sénégal'),
        ('SYC', 'Seychelles'),
        ('SLE', 'Sierra Leone'),
        ('SOM', 'Somalie'),
        ('ZAF', 'Afrique du Sud'),
        ('SSD', 'Soudan du Sud'),
        ('SDN', 'Soudan'),
        ('TZA', 'Tanzanie'),
        ('TGO', 'Togo'),
        ('TUN', 'Tunisie'),
        ('UGA', 'Ouganda'),
        ('ZMB', 'Zambie'),
        ('ZWE', 'Zimbabwe'),
    ]

    nom_recette = models.CharField(max_length=500)
    image = models.ImageField(upload_to="recettes_images/", blank=False, null=False)
    pays = models.CharField(max_length=3, choices=PAYS_AFRIQUE)
    prix = models.IntegerField(default=0)
    description = description = models.TextField(blank=False, null=False)
    temps_preparation = models.IntegerField(blank=False, null=False)
    date_creation = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.nom_recette

# les ingredients nécessaire à chaque recette

class Ingredient(models.Model):
    nom_ingredient = models.CharField(max_length=200)
    quantite = models.CharField(max_length=500) 
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, blank=True)
    unite = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.nom_ingredient
    
class Etape(models.Model):
    description = models.TextField()  
    ordre = models.IntegerField()  
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE, related_name='etapes')
    duree_estimee = models.IntegerField(blank=True, null=True)  


    def __str__(self):
        return f"Étape {self.ordre} : {self.description[:20]}..."
    
# le modèle pour les utilisateurs


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return f"Profil de {self.user.username}"
  
# une classe pour gerer les commandes passer par l'utilisateur
 
class Order(models.Model):
    recette= models.ForeignKey(Recette,  on_delete=models.CASCADE) 
    customer = models.ForeignKey(User, on_delete=models.CASCADE) 
    quantity = models.IntegerField(default=1) 
    price = models.IntegerField(default=1) 
    address = models.CharField(max_length=50, default='', blank=True) 
    phone = models.CharField(max_length=50, default='', blank=True) 
    date = models.DateField(default=datetime.datetime.today) 
    status = models.BooleanField(default=True) 
    mode_paiement = models.CharField(max_length=50, choices=[('Carte', 'Carte Bancaire'), ('Espèces', 'Espèces'), ('En Ligne', 'Paiement en Ligne')])

   
# pour les commentaires

class Commentaire(models.Model):
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE, related_name='commentaires')  
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)  
    contenu = models.TextField()  
    date_creation = models.DateTimeField(auto_now_add=True) 
    note = models.IntegerField(blank=True, null=True, choices=[(1, '★'), (2, '★★'), (3, '★★★'), (4, '★★★★'), (5, '★★★★★')])
    # pour replies entre commentaire
    parent_commentaire = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='replies')


    def __str__(self):
        return f"Commentaire de {self.utilisateur}"
    
