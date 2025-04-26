
### **Saveurs Africaines - Application Culinaire Interactive**

**Saveurs Africaines** est une application web conçue pour explorer, apprendre, et commander des plats africains authentiques. Elle met l'accent sur la richesse de la cuisine africaine, en offrant des fonctionnalités interactives adaptées aux amateurs de gastronomie.

---

### **🛠️ Fonctionnalités Principales**

#### 📝 **Catalogue de Recettes**
- **Par pays** : Explorez des plats selon leur origine géographique (Sénégal, Côte d’Ivoire, Ghana, etc.).  
- **Détails complets** : Ingrédients, étapes de préparation détaillées, photos/vidéos, et anecdotes culturelles.  
- **Filtre intelligent** : Trouvez des recettes basées sur les ingrédients que vous avez sous la main.

#### 📚 **Mode d’Apprentissage Culinaire**
- Guide interactif pour apprendre à cuisiner les plats en suivant les instructions étape par étape.  
- Possibilité de marquer des recettes comme favorites ou téléchargées pour un usage hors ligne.

#### 🛒 **Commande en Ligne**
- Ajoutez des plats à votre panier et passez des commandes rapidement.  
- Notifications en temps réel pour le suivi des commandes.  

#### 🔍 **Recherche Avancée**
- Recherchez par nom de plat, ingrédients, ou catégorie.  
- Suggestions intelligentes basées sur vos préférences ou votre historique de recherche.

#### 📊 **Planification des Repas**
- Organisez votre semaine avec un calendrier culinaire.  
- Recevez des suggestions pour optimiser vos repas en fonction des recettes sélectionnées.

#### 🎉 **Jeux et Concours**
- Participez à des concours culinaires avec d'autres utilisateurs.  
- Gagnez des points ou des bons de réduction pour vos créations.

#### 🖥️ **Communauté et Partage**
- Publiez vos photos de plats et partagez vos astuces culinaires.  
- Intégrez vos réseaux sociaux pour inspirer les autres utilisateurs.  

#### 💡 **Fonctionnalités Supplémentaires**
- **Mode Hors Ligne** : Téléchargez des recettes pour les consulter sans connexion internet.  
- **Calculateur Nutritionnel** : Obtenez des informations sur les valeurs nutritionnelles des plats.

---

### **📁 Structure du Projet**

```plaintext
Saveurs-Africaines/
├── backend/                # Code Django pour le backend
│   ├── models.py           # Modèles pour recettes, utilisateurs, commandes
│   ├── views.py            # Gestion des API REST
│   ├── serializers.py      # Sérialisation des données
│   └── urls.py             # Routes pour les fonctionnalités backend
├── frontend/               # Application React.js pour le frontend
│   ├── components/         # Composants React (formulaires, cartes, navigation)
│   ├── pages/              # Pages principales (Accueil, Recettes, Profil)
│   ├── App.js              # Point d’entrée de l’application
│   └── index.js            # Fichier principal React
├── database/               # Configuration PostgreSQL
└── README.md               # Documentation du projet
```

---

### **⚙️ Installation et Lancement**

#### Backend (Django) :
1. **Clonez le dépôt :**
   ```bash
   git clone https://github.com/username/saveurs-africaines.git
   cd saveurs-africaines/backend
   ```
2. **Installez les dépendances :**
   ```bash
   python -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   ```
3. **Configurez la base de données :**
   - Configurez PostgreSQL dans `settings.py`.
   - Appliquez les migrations :
     ```bash
     python manage.py migrate
     ```
4. **Lancez le serveur :**
   ```bash
   python manage.py runserver
   ```

#### Frontend (React.js) :
1. **Accédez au dossier frontend :**
   ```bash
   cd ../frontend
   ```
2. **Installez les dépendances :**
   ```bash
   npm install
   ```
3. **Lancez l’application :**
   ```bash
   npm start
   ```

---

### **💡 Utilisation**

- **Accueil :** Découvrez les plats populaires et les nouveautés.  
- **Recherche :** Utilisez l’option de recherche avancée pour trouver des recettes facilement.  
- **Apprentissage :** Suivez les étapes pour cuisiner un plat comme un pro.  
- **Commande :** Commandez vos plats préférés directement via l’application.  
- **Statistiques :** Consultez vos recettes favorites et suivez vos commandes.  

---

### **🤝 Contribution**

Les contributions sont toujours les bienvenues ! Vous pouvez :
- Signaler des bugs.  
- Proposer des fonctionnalités.  
- Soumettre des pull requests.

---

### **📫 Contact**

- **Email :** nwolle14@gmail.com  
- **YouTube :** yankeecode

---

### **📄 Licence**
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus d’informations.

---
