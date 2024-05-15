from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sei_la(request):
    return HttpResponse('<h1>ok</h1>')