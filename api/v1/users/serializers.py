from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    # ユーザを作る際に使用するcreateメソッドをオーバーライドする。
    def create(self, validated_data):
        # パスワードをハッシュ化する
        user = User.objects.create_user(**validated_data)
        # トークンを生成する
        Token.objects.create(user=user)
        return user
