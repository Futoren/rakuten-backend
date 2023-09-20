from django.db import models

from ingredient.models import Ingredient


class Recipe(models.Model):
    title = models.CharField(max_length=200)   # レシピのタイトル
    ingredients_grams = models.ManyToManyField(
        Ingredient, through='RecipeIngredient')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    grams = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.ingredient.name} ({self.grams}g)"
