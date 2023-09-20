from django.urls import path
from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from .chat.views import ChatViewSet
from .ingredients.views import IngredientViewSet
from .menu.views import MenuViewSet
from .menu_suggestion.views import MenuSuggestionViewSet
from .recipe.views import RecipeViewSet
from .recipe.views import RecipeIngredientViewSet
from .user_info.views import UserInfoViewSet
from .users.views import ManageUserView, UserViewSet


router = routers.DefaultRouter()
router.register('users', UserViewSet, basename="User")
router.register('chat', ChatViewSet, basename="Chat")
router.register('ingredient', IngredientViewSet, basename="Ingredient")
router.register('recipe', RecipeViewSet, basename="Recipe")
router.register('recipeIngredients', RecipeIngredientViewSet, basename="RecipeIngredients")
router.register('menu_suggestion', MenuSuggestionViewSet,basename="MenuSuggestion")
router.register('menu', MenuViewSet, basename="Menu")
router.register('user_info', UserInfoViewSet, basename="UserInfo")

urlpatterns = [
    path('myself/', ManageUserView.as_view(), name='myself'),
    # ユーザ名とパスワードをPOSTするとトークンを返す。
    path('', include(router.urls)),
]
