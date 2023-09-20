from rest_framework import serializers
from ingredient.models import Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'category', 'expiration_date', 'created_at']
