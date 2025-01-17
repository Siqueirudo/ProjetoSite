from django.db import models

# Create your models here.

CATEGORY_CHOICES = [
    ('camisas', 'Camisas'),
    ('casacos', 'Casacos'),
    ('calcas', 'Calças_Bermudas'),]

SIZE_CHOICES = [
    ('P', 'Pequeno'),
    ('M', 'Médio'),
    ('G', 'Grande'),
    ('GG', 'Extra Grande'),]

class cloth(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    category = models.CharField(max_length=10,choices=CATEGORY_CHOICES,blank=True,null=True)
    size = models.CharField(max_length=6,choices=SIZE_CHOICES)
    value = models.FloatField(blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    photo1 = models.ImageField(upload_to='cars/',blank=True, null=True)
    photo2 = models.ImageField(upload_to='cars/',blank=True, null=True)
    photo3 = models.ImageField(upload_to='cars/',blank=True, null=True)
    

    def __str__(self):
        return self.model