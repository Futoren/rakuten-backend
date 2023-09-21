import json

from django.http import QueryDict, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets

from user_info.models import UserInfo

from .serializers import UserInfoSerializer


class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer


@csrf_exempt
def update_user_info(request, user_info_id):
    # ユーザーを特定
    user_info = get_object_or_404(UserInfo, pk=user_info_id)
    if request.method == 'PUT':
        try:
            # JSONデータを解析
            data = json.loads(request.body)
            # 更新対象のフィールドを設定
            if 'disliking_ingredients' in data:
                new_disliking_ingredients_ids = data['disliking_ingredients']
                user_info.disliking_ingredients.set(new_disliking_ingredients_ids)

            if 'allergy' in data:
                new_allergy_ids = data['allergy']
                user_info.allergy.set(new_allergy_ids)

            # 保存して更新を反映
            user_info.save()

            # 成功応答
            return JsonResponse({'message': 'User info updated successfully'})
        except json.JSONDecodeError as e:
            # JSON解析エラー時のエラー応答
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    else:
        # PUT以外のリクエストに対するエラー応答
        return JsonResponse({'error': 'Only PUT requests are allowed'}, status=400)
