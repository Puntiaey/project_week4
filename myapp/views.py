from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Car,Rent
from .models import Person
from .forms import PersonForm
from .forms import CarForm

# Create your views here.

def home(request):
	return render(request, 'home.html')
	
def list(request):
	return render(request, 'list.html')

class CreatePersonView(CreateView):
	queryset = Person()
	template_name='create.html'
	form_class = PersonForm
	success_url = '/admin'

class CreateCarView(CreateView):
	queryset = Car()
	template_name='rentcar.html'
	form_class = CarForm
	success_url = '/admin'

class ListPersonView(ListView):
    model = Person

class CarListView(ListView):
    model = Car
    template_name='car_list.html'

class RentListView(ListView):
    model = Rent
    template_name='rent_list.html'
