from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def about(request):
    context = {
        'title': 'description'
    }
    return render(request,'about.html', context)
