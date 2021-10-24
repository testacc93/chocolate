from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Chocolate
from . import models
# Create your views here.
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
    return render(request, 'contact.html')