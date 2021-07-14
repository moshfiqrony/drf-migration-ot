from django.db import models
from avenger.models import AvengerUser


# Create your models here.
class BlackOrderUser(models.Model):
    username = models.CharField(max_length=256, null=True, default=None)
    killed_by = models.ForeignKey(AvengerUser, on_delete=models.CASCADE, null=True, default=None, related_name='black_order_killed_by')
