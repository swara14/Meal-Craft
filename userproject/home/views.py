from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
import requests
from .forms import CreateUserForm

# Remove the import of _Authenticator from imaplib
# from imaplib import _Authenticator

# Remove the import of _Authenticator from Django auth
# from django.contrib.auth import _Authenticator

# Create your views here.

def index(request):
    return render(request, 'index.html')

def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index.html')

    context={}            
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('index.html')

def user_signin(request):
    form = CreateUserForm()

    if request.method=='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login.html')

    context={'form' : form}
    return render(request, 'signin.html', context)

def random_recipe(request):
    # Define the API URL
    api_url = "https://api.spoonacular.com/recipes/random?apiKey=c4b21d87d23543f0b7aa54686bd93809"

    # Send a GET request to the API URL
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        recipe_data = response.json()
        
        # Extract the recipe details
        recipe = recipe_data["recipes"][0]
        
        # Prepare context data to pass to the template
        context = {
            "recipe_title": recipe["title"],
            "ingredients": [ingredient["original"] for ingredient in recipe["extendedIngredients"]],
            "instructions": [step["step"] for step in recipe["analyzedInstructions"][0]["steps"]],
            "source_url": recipe["sourceUrl"]
        }
        
        # Render the template with the context data
        return render(request, 'random-recipe.html', context)

def select_ingredients(request):
    if request.method == 'POST':
        ingredients = request.POST.get('ingredients')
        ingredients = ','.join(ingredients.split())  # Convert spaces to commas
        api_key = 'c4b21d87d23543f0b7aa54686bd93809'
        url = f'https://api.spoonacular.com/recipes/findByIngredients?apiKey={api_key}&ingredients={ingredients}&number=15'
        
        response = requests.get(url)
        recipes = response.json()
        
        return render(request, 'results.html', {'recipes': recipes})
    
    return render(request, 'search.html')

# def recipe_detail(request, recipe_id):
#     api_key = 'c4b21d87d23543f0b7aa54686bd93809'
#     url = f'https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={api_key}'

#     response = requests.get(url)
#     data = response.json()

#     context = {
#         'recipe_id': data['id'],
#         'recipe_name': data['title'],
#         'image': data['image'],
#         'servings': data['servings'],
#         'ready_in_minutes': data['readyInMinutes'],
#         'dish_type': ', '.join(data['dishTypes']),
#         'ingredients': data['extendedIngredients'],
#         'instructions': data['instructions']
#     }

#     return render(request, 'recipe_detail.html', context)

# @login_required
# def save_recipes(request, recipe_id):
#     if request.method=='POST':
#         recipe = Recipe.objects.get(pk=recipe_id)
#         profile = request.user.userprofile
#         profile.saved_recipes.add(recipe)
#         return redirect('results.html', recipe_id=recipe_id)
#     else:
#         pass    

# @login_required
# def display_saved_recipes(request):
#     profile = request.user.userprofile
#     saved_recipes= profile.saved_recipes.all()
#     return render(request, 'saved_recipes.html', {'saved_recipes': saved_recipes})