from rest_framework import serializers

from menu_suggestion.models import MenuSuggestion


class MenuSuggestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuSuggestion
        fields = '__all__'
