from django.db import models

from ingredient.models import Ingredient


class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    grams = models.IntegerField()


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    recipe_ingredient = models.ManyToManyField(
        RecipeIngredient, related_name='recipes_ingredient')
    created_at = models.DateTimeField(auto_now_add=True)
    img_url = models.CharField(max_length=200, null=True)
