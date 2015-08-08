import django import forms

class ContactForm(forms.Form):
	name = forms.CharField(max_length=150)
	telephone = forms.CharField(max_length=100)
	email = forms.EmailField(max_length=100)
	mensaje = forms.TextField()