from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from user_info.models import UserInfo

from .serializers import UserInfoSerializer


class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
