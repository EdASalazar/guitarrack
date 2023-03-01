from django.db import models

# Create your models here.
class Guitar(models.Model):
    brand = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    year = models.DateField()
    color = models.CharField(max_length=100)
    numPickups = models.IntegerField()
    typePickups = models.CharField(max_length=200)
    def __str__(self):
        return f'{self.brand} {self.make} {self.year}'