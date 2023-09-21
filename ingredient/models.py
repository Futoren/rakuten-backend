from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    expiration_date = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    trivia_url = models.CharField(max_length=200, null=True)
