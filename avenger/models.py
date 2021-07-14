from django.db import models

# Create your models here.
class AvengerUser(models.Model):
    name = models.CharField(max_length=256, null=True, default=None)
    email = models.CharField(max_length=256, default=None, null=True)
    address = models.CharField(max_length=256, default=None, null=True)
    address1 = models.CharField(max_length=256, default=None, null=True)