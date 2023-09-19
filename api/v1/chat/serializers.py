from rest_framework import serializers
from chat.models import Chat


class ChatSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Chat
        fields = ['id', 'author', 'body', 'created_at']
