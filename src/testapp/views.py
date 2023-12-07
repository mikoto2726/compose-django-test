from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def root(request):
    return HttpResponse('Hello Django and Docker')

def goodbye(request):
    return render(request, 'index.html')