from home import views
from django.contrib import admin
from django.urls import path, include
# from .views import random_recipe

urlpatterns = [
    path('', views.index, name='home'),
    path('index.html', views.index, name='home'),
    path('login.html', views.user_login, name="login"),
    path('logout', views.user_logout, name='logout'),
    path('signin.html', views.user_signin, name="signin"),
    path('random-recipe.html', views.random_recipe, name="random-recipe"),
    path('search.html', views.select_ingredients, name="recipe_search"),
    # path('save_recipes.html', views.save_recipes, name='save_recipes'),
    # path('saved_recipes.html', views.display_saved_recipes, name='saved_recipes')
]
