from django.shortcuts import render, redirect 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, CreateView
from .models import Guitar, Pedal
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
    id_list = guitar.pedals.all().values_list('id')
    pedals_guitar_doesnt_have = Pedal.objects.exclude(id__in=id_list)
    restringing_form = RestringingForm()
    return render(request, 'guitars/detail.html', 
                  { 'guitar': guitar, 'restringing_form': restringing_form, 
                   'pedals': pedals_guitar_doesnt_have })

class GuitarCreate(CreateView):
    model = Guitar
    fields = '__all__'

class GuitarUpdate(UpdateView):
    model = Guitar
    fields = ['make', 'color']

class GuitarDelete(DeleteView):
    model = Guitar
    success_url = '/guitars'

def add_strings(request, guitar_id):
    form = RestringingForm(request.POST)
    if form.is_valid():
        new_strings = form.save(commit=False)
        new_strings.guitar_id = guitar_id
        new_strings.save()
    return redirect('detail', guitar_id=guitar_id)


class PedalList(ListView):
    model = Pedal

class PedalDetail(DetailView):
    model = Pedal

class PedalCreate(CreateView):
    model = Pedal
    fields = '__all__'

class PedalUpdate(UpdateView):
    model = Pedal
    fields = '__all__'

class PedalDelete(DeleteView):
    model = Pedal
    success_url = '/pedals'