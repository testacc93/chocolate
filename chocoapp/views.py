from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Chocolate, Query
from . import models
from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.contrib import messages
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def shop(request):
    all_chocolates = Chocolate.objects.all()
    all_chocolates_list = []
    for chocolate in all_chocolates:
        all_chocolates_list.append(chocolate)
    print(all_chocolates)
    context = {
        'all_chocolates': all_chocolates_list
    }
    return render(request, 'shop.html', context)

def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print("efkne",form.cleaned_data)
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['Message']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            print(subject)
            Query.objects.create(name=name, email=email, subject=subject, message=message)
            context = {
                'form':form,
                'message': 'Your message is received, will get back to you soon.'
            }
            return render(request, 'contact.html', context)

    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form':form})