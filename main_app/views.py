from django.shortcuts import render
from django.http import HttpResponse

guitars = [
    {'name': 'Gibson', 'bridge_pickup': 'humbucker'},
    {'name': 'Strat', 'bridge_pickup': 'single coil'},
]


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def guitars_index(request):
    return render(request, 'guitars/index.html', {
        'guitars': guitars        
    })

