from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    context = {
        'name':'Rafi',
        'university': 'American International University Bangladesh',
        'age' : 26,
        'city': 'Dhaka',
        'country': 'Bangladesh',
        'passion':'Data Science',
    }
    return render(request, 'index.html', context)
