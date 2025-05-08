<template>
  <div class="app-container">
    <!-- Header -->
    <header class="header">
      <div class="header_logo">
        <p class="header_logo_title">Restaurant Africains</p>
      </div>
      <nav class="navbar_menu">
        <a href="#" class="navbar_menu_link">Accueil</a>
        <a href="#" class="navbar_menu_link">Actus</a>
        <a href="#" class="navbar_menu_link">Top Chefs</a>
        <a href="#" class="navbar_menu_link">Restaurants</a>
        <a href="#" class="navbar_menu_link">meilleurs Recettes</a>

      </nav>
    </header>

    <!-- Hero -->
    <section class="hero">
      <h1>Découvrez les meilleurs plats africains !</h1>
      <p>Plus de 90 000 recettes faciles et rapides pour vous inspirer en cuisine.</p>
      <button class="cta">Explorer maintenant</button>
    </section>

    <!-- Recettes -->
    <section class="featured-recipes">
      <h2>Plats populaires</h2>
      <div class="recipe-grid">
        <div v-for="recette in recettes" :key="recette.id" class="recipe-card">
          <img :src="recette.image" alt="image recette" class="recipe-image" />
          <h3>{{ recette.nom_recette }}</h3>
          <p>{{ recette.description.slice(0, 80) }}...</p>
          <span class="price">{{ recette.prix }} FCFA</span>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
      <p>&copy; 2025 Restaurant Africains. Tous droits réservés.</p>
    </footer>
  </div>
</template>
