from django.db import models
from apps.accounts.models import MainUser


class PointsManager(models.Model):
    account = models.OneToOneField(
        MainUser, on_delete=models.CASCADE, related_name='points')
    total = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f'Puntos - {self.account.name}'

    def add_points(self, points: int):
        self.total + points
        self.save()

    def redeem_points(self, points: int):
        self.total - points
        if self.total < 0:
            return False
        self.save()
