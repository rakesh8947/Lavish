from django.shortcuts import render
from django.views.generic import ListView
from .models import Office
from django.shortcuts import render, redirect
from django.http import *
from .forms import ContactForm
from .models import Scontact

# Create your views here.
#def base(request):
	#return render(request, 'base.html' )

class HomePageView(ListView):
	model = Office	
	template_name = 'index.html'

def thanks(request):
	return render(request, 'thanks.html')

def register(request):
	return render(request, 'register/register.html')


def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			Name = form.cleaned_data['Name']
			Lname = form.cleaned_data['Lname']
			Contact = form.cleaned_data['Contact']
			Email = form.cleaned_data['Email']
			Message = form.cleaned_data['Message']
			form.save()
			return redirect('/thanks/')
	else:
		form = ContactForm()
	return render(request, 'contact.html')

