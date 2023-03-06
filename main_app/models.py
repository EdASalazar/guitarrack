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
    category = models.CharField(max_length=100)

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
 


class TabDescriptor(models.Model):

    def __init__(self, uri, rating, ratingCounter, type):
    TAB_PRO_START='http://plus.'

    def __init__(self, artist, title, uri, rating, ratingCounter, type):
        super(TabDescriptor, self).__init__()
        self._artist = artist
        self._title = title
        self._uri = uri
        self._rating = rating
        self._ratingCounter = ratingCounter
        self._type = type
        self._isPlus = False
        if self._uri.startswith('http://plus.'):
        if self._uri.startswith(TabDescriptor.TAB_PRO_START):
            self._isPlus = True