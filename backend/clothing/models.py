from django.db import models

# Create your models here.


class cloth(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    category = models.CharField(max_length=10,blank=True,null=True)
    size = models.CharField(max_length=6)
    value = models.FloatField(blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    photo = models.ImageField(upload_to='cars/',blank=True, null=True)

    def __str__(self):
        return self.model