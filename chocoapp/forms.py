from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    email = forms.CharField(label='Your email', max_length=100)
    subject = forms.CharField(label='Subject', max_length=100)
    Message = forms.CharField(label='Message', max_length=100)
    