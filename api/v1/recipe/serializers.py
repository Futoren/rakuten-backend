from incredients.serializers import IngredientSerializer
from rest_framework import serializers

from recipe.models import Recipe, RecipeIngredient


class RecipeIngredientSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer()

    class Meta:
        model = RecipeIngredient
        fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):
    ingredients_grams = RecipeIngredientSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = '__all__'
