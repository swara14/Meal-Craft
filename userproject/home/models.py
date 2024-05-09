from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# class Recipe(models.Model):
#     title= models.CharField(max_length=100)
#     ingredients = models.TextField()
#     instuctions = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title
    
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     saved_recipes = models.ManyToManyField(Recipe)

#     def __str__(self):
#         return self.user.username
