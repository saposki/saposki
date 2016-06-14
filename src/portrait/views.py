from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from . models import Portrait

def portrait(request):
    queryset = Portrait.objects.all()
    context = {
        'image' : queryset
    }
    return render(request, 'portrait.html', context)

def portrait_detail(request):
    # instance = get_object_or_404(Portait, title="abc")
    context = {
        # 'title': instance.title,
        # 'instance': instance
    }
    return render(request, 'portrait_detail.html', context)
