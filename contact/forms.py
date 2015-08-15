from django import forms

class ContactForm(forms.Form):
	name = forms.CharField(max_length=100, required=True)
	telephone = forms.CharField(max_length=100, required=True)
	email = forms.EmailField(max_length=100, required=True)
	mensaje = forms.CharField(widget=forms.Textarea, required=True)