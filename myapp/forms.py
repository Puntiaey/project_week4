from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
#from django.forms.extras.widgets import SelectDateWidget
from django.contrib.admin import widgets
import datetime
from .models import Person,Car,Rent

class PersonForm(ModelForm):
	class Meta:
		model = Person
		exclude=[]
	def __init__(self, *args, **kwargs):
		super(PersonForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit', 'Submit'))

class CarForm(ModelForm):
 class Meta:
  model =  Car
  exclude=[]

 def __init__(self, *args, **kwargs):
  super(CarForm, self).__init__(*args, **kwargs)
  self.helper = FormHelper()
  self.helper.add_input(Submit('submit', 'Submit'))

class RentForm(ModelForm):
	class Meta:
		model =  Rent
		exclude=[]
	def __init__(self, *args, **kwargs):
		super(RentForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit', 'Submit'))
