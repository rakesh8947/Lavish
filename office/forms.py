from django import forms
from .models import Scontact

class ContactForm(forms.ModelForm):
	class Meta:
		model = Scontact
		fields = ['Name','Lname','Contact','Email','Message']