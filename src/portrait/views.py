from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from . models import Portrait

def portrait(request):
    queryset = Portrait.objects.all()
    context = {
        'image' : queryset
    }
    return render(request, 'portrait.html', context)
