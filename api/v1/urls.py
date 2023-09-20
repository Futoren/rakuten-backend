from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .users.views import UserViewSet, ManageUserView
from .chat.views import ChatViewSet
from .ingredients.views import IngredientViewSet
from .recipe.views import RecipeViewSet
from .recipe.views import RecipeIngredientsViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet, basename="User")
router.register('chat', ChatViewSet, basename="Chat")
router.register('ingredient', IngredientViewSet, basename="Ingredient")
router.register('recipe', RecipeViewSet, basename="Recipe")
router.register('recipeIngredients', RecipeIngredientsViewSet, basename="RecipeIngredients")


urlpatterns = [
    path('myself/', ManageUserView.as_view(), name='myself'),
    # ユーザ名とパスワードをPOSTするとトークンを返す。
    path('', include(router.urls)),
]
