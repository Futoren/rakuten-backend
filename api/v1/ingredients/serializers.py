from rest_framework import serializers
from ingredients.models import Ingredients

class ChatSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Ingredients
        fields = []
