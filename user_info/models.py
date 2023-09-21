from django.db import models

from ingredient.models import Ingredient


class UserInfo(models.Model):
    GENDER_CHOICES = [
        ('M', '男性'),
        ('F', '女性'),
        ('N', 'その他'),
    ]

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    addredss = models.CharField(max_length=200)
    # 嫌いな食材との多対多の関係を定義
    disliking_ingredients = models.ManyToManyField(
        Ingredient, related_name='disliking_ingredients')
    # アレルギー
    allergy = models.ManyToManyField(Ingredient, related_name='allergy')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
