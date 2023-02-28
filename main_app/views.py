from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def index(request):
    return HttpResponse("Hello, world. You're at the guitars index.")

def about(request):
    return render(request, 'about.html')