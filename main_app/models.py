from django.db import models
from django.urls import reverse

STRINGS = (
    ('NP', 'Nickel-plated steel'),
    ('PN', 'Pure nickel'),
    ('SS', 'Stainless steel'),
    ('NY', 'Nylon'),
)

# Create your models here.
class Guitar(models.Model):
    brand = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.brand} {self.make}'
    def get_absolute_url(self):
        return reverse('detail', kwargs={'guitar_id': self.id})
    
class Restringing(models.Model):
    date = models.DateField('Date Changed')
    String = models.CharField(
        max_length=2,
        choices=STRINGS,
        default=STRINGS[0][0]
        )
    guitar = models.ForeignKey(Guitar, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.get_string_display()} on {self.date}"
    