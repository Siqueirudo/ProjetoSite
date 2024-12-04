from django.db import models

# Create your models here.

class cloth(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    size = models.CharField(max_length=4)
    value = models.IntegerField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)