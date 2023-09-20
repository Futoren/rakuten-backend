from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from ingredient.models import Ingredient
from .serializers import IngredientSerializer


# Create your views here.

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
