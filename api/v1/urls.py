from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .users.views import UserViewSet, ManageUserView
from .chat.views import ChatViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet, basename="User")
router.register('chat', ChatViewSet, basename="Chat")

urlpatterns = [
    path('myself/', ManageUserView.as_view(), name='myself'),
    # ユーザ名とパスワードをPOSTするとトークンを返す。
    path('', include(router.urls)),
]
