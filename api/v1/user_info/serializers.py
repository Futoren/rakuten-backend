from rest_framework import serializers

from user_info.models import UserInfo


class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserInfo
        fields = '__all__'
