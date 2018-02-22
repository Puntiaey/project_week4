from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Car,Rent
from .models import Person
from .forms import PersonForm

# Create your views here.

def home(request):
	return render(request, 'home.html')
	
def creates(request):
	return render(request, 'create.html')

def list(request):
	return render(request, 'list.html')

class CreatePersonView(CreateView):
	queryset = Person()
	template_name='create.html'
	form_class = PersonForm
	success_url = '/admin'

class CarListView(ListView):
    model = Car
    template_name='car_list.html'

class RentListView(ListView):
    model = Rent
    template_name='rent_list.html'