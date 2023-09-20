from rest_framework import viewsets

from menu_suggestion.models import MenuSuggestion

from .serializers import MenuSuggestionSerializer


class MenuSuggestionViewSet(viewsets.ModelViewSet):
    queryset = MenuSuggestion.objects.all()
    serializer_class = MenuSuggestionSerializer
