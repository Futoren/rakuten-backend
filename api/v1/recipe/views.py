from rest_framework import viewsets
from recipe.models import Recipe, RecipeIngredient
from .serializers import RecipeSerializer
from .serializers import RecipeIngredientSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeIngredientViewSet(viewsets.ModelViewSet):
    queryset = RecipeIngredient.objects.all()
    serializer_class = RecipeIngredientSerializer
