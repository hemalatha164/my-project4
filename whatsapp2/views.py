from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def ramesh(request):
    return HttpResponse('<h2>eating 5star chocolate with suresh</h2>')