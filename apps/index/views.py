from django.shortcuts import render

# Create your views here.
from django.template.context_processors import request


def IndexView(request):
    ctx={}
    return render(request, "index/index.html", ctx)