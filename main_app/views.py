from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Guitar
from .forms import RestringingForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def guitars_index(request):
    guitars = Guitar.objects.all()
    return render(request, 'guitars/index.html', {
        'guitars': guitars        
    })

def guitars_detail(request, guitar_id):
    guitar = Guitar.objects.get(id=guitar_id)
    restringing_form = RestringingForm()
    return render(request, 'guitars/detail.html', 
                  { 'guitar': guitar, 'restringing_form': restringing_form })

class GuitarCreate(CreateView):
    model = Guitar
    fields = '__all__'

class GuitarUpdate(UpdateView):
    model = Guitar
    fields = ['make', 'color']

class GuitarDelete(DeleteView):
    model = Guitar
    success_url = '/guitars'

