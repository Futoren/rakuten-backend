from django.db import models

from menu.models import Menu
from user_info.models import UserInfo


class MenuSuggestion(models.Model):
    user_info = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    arrived_date = models.DateTimeField()
