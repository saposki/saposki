from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from . models import Crasher

def crasher(request):
    queryset = Crasher.objects.all()
    context = {
        'image' : queryset
    }
    return render(request, 'crasher.html', context)

def crasher_detail(request):

    context = {


    }
    return render(request, 'crasher_detail.html', context)
