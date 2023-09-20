from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from recipe.models import Recipe

from .serializers import RecipeSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
