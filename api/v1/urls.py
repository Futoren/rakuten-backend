from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from .chat.views import ChatViewSet
from .ingredients.views import IngredientViewSet
from .menu.views import MenuViewSet
from .menu_suggestion.views import MenuSuggestionViewSet, get_ingredient
from .recipe.views import RecipeViewSet, RecipeIngredientViewSet
from .user_info.views import UserInfoViewSet, update_user_info
from .users.views import ManageUserView, UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet, basename="User")
router.register('chat', ChatViewSet, basename="Chat")
router.register('ingredient', IngredientViewSet, basename="Ingredient")
router.register('recipe', RecipeViewSet, basename="Recipe")
router.register('recipeIngredient', RecipeIngredientViewSet, basename="RecipeIngredient")
router.register('menu_suggestion', MenuSuggestionViewSet,basename="MenuSuggestion")
router.register('menu', MenuViewSet, basename="Menu")
router.register('user_info', UserInfoViewSet, basename="UserInfo")

urlpatterns = [
    path('myself/', ManageUserView.as_view(), name='myself'),
    path('get_ingredient/<int:menu_suggestion_id>/', get_ingredient, name='get_ingredient_ids'),
    path('update_user_info/<int:user_info_id>/', update_user_info, name='update_user_info'),
    # ユーザ名とパスワードをPOSTするとトークンを返す。
    path('', include(router.urls)),
]
