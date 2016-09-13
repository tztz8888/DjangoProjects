from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

def index(request):
    return render(request, 'index.html')

def result(request):
    return render(request, 'result.html')

def good(request):
    return render(request, 'good.html')
# Create your views here.