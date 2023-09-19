from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from chat.models import Chat
from .serializers import ChatSerializer


class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (IsAuthenticated,)
