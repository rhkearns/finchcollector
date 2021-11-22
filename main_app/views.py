from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Finch, House
from .forms import SightingForm
# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  finches = Finch.objects.all()
  return render(request, 'finches/index.html', { 'finches': finches })

def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  sighting_form = SightingForm()
  return render(request, 'finches/detail.html', { 'finch': finch, 'sighting_form' : sighting_form })

class FinchCreate(CreateView):
  model = Finch
  fields = ['name', 'variety', 'description', 'age']

class FinchUpdate(UpdateView):
  model = Finch
  fields = ['variety', 'description', 'age']

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches/'

def add_sighting(request, finch_id):
  form = SightingForm(request.POST)
  if form.is_valid():
    new_sighting = form.save(commit=False)
    new_sighting.finch_id = finch_id
    new_sighting.save()
  return redirect('finches_detail', finch_id=finch_id)

class HouseCreate(CreateView):
  model = House
  fields = '__all__'

class HouseList(ListView):
  model = House

class HouseDetail(DetailView):
  model = House

class HouseUpdate(UpdateView):
  model = House
  fields = ['name', 'color']

class HouseDelete(DeleteView):
  model = House
  success_url = '/houses/'