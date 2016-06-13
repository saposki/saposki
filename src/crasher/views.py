from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from . models import Crasher

def crasher(request):
    queryset = Crasher.objects.all()
    context = {
        'image' : queryset
    }
    return render(request, 'crasher.html', context)
