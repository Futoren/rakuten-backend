from datetime import timedelta

from django.http import JsonResponse
from rest_framework import viewsets

from ingredient.models import Ingredient
from menu_suggestion.models import MenuSuggestion

from .serializers import MenuSuggestionSerializer


class MenuSuggestionViewSet(viewsets.ModelViewSet):
    queryset = MenuSuggestion.objects.all()
    serializer_class = MenuSuggestionSerializer


def get_menu(request, menu_suggestion_id):
    try:
        menu_suggestion = MenuSuggestion.objects.get(pk=menu_suggestion_id)
        recipes = menu_suggestion.menu.recipes.all()
        recipe_list = []
        for recipe in recipes:
            recipe_ingredients = recipe.recipe_ingredient.all()
            recipe_data = {
                'recipe_name': recipe.title,
                'recipe_img': recipe.img_url,
                'ingredients': [
                    {
                        'ingredient_name': ingredient.ingredient.name,
                        'grams': ingredient.grams,
                    }
                    for ingredient in recipe_ingredients
                ],
            }
            recipe_list.append(recipe_data)
        return JsonResponse({'recipes': recipe_list})
    except MenuSuggestion.DoesNotExist:
        return JsonResponse({'error': 'MenuSuggestion not found'}, status=404)


def get_ingredient(request, menu_suggestion_id):
    try:
        menu_suggestion = MenuSuggestion.objects.get(pk=menu_suggestion_id)
        ingredients = menu_suggestion.menu.recipes.values_list('recipe_ingredient__ingredient', flat=True)
        ingredient_objects = Ingredient.objects.filter(id__in=ingredients)
        ingredient_list = [{'id': ingredient.id, 'name': ingredient.name,
                            'url': ingredient.trivia_url,
                            'arrived_date': menu_suggestion.arrived_date,
                            'expiration_date': menu_suggestion.arrived_date + timedelta(
                                days=ingredient.expiration_date)}
                           for ingredient in ingredient_objects]
        return JsonResponse({'ingredients': ingredient_list})
    except MenuSuggestion.DoesNotExist:
        return JsonResponse({'error': 'MenuSuggestion not found'}, status=404)
