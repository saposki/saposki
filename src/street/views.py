from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from . models import Street

def street(request):
    queryset = Street.objects.all()
    context = {
        'image' : queryset
    }
    return render(request, 'street.html', context)

def street_detail(request):

    context = {


    }
    return render(request, 'street_detail.html', context)
