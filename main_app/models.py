from django.db import models
from django.urls import reverse
from datetime   import date

STRINGS = (
    ('NP', 'Nickel-plated steel'),
    ('PN', 'Pure nickel'),
    ('SS', 'Stainless steel'),
    ('NY', 'Nylon'),
)

# Create your models here.
class Pedal(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    catagory = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.brand}: {self.name}'
    
    def get_absolute_url(self):
        return reverse('pedals_detail', kwargs={'pk': self.id})
    


class Guitar(models.Model):
    brand = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    pedals = models.ManyToManyField(Pedal)

    def __str__(self):
        return f'{self.brand} {self.make}'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'guitar_id': self.id})
    
class Restringing(models.Model):
    date = models.DateField('Date Changed')
    string = models.CharField(
        max_length=2,
        choices=STRINGS,
        default=STRINGS[0][0]
        )
    
    guitar = models.ForeignKey(Guitar, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.get_string_display()} on {self.date}"
    
    class Meta: 
        ordering = ['-date']
 