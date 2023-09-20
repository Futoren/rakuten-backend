from django.db import models

from recipe.models import Recipe


class Menu(models.Model):
    recipes = models.ManyToManyField(Recipe, related_name='menus')
    created_at = models.DateTimeField(auto_now_add=True)
