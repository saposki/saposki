from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from . models import About

def about(request):
    queryset = About.object.all()
    context = {
        'title': 'about'
    }
    return render(request,'about.html', context)
