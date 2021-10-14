from django.db import models
from apps.accounts.models import MainUser


class PointsManager(models.Model):
    account = models.OneToOneField(
        MainUser, on_delete=models.CASCADE, related_name='points')
    total = models.PositiveIntegerField(default=0)
