from django.http.request import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def show_title(request):
    return render(request, 'home.html', {})
