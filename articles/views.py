from django.http.request import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def show_title(request):
    return render(request, 'home.html', {})


def obratka(slovo):
    slovo = 'zhopa'
    for i in range(len(slovo) - 1, -1, -1):
        return slovo[i]

def reverse(request):
    # test_get_text = request.GET['usertext']
    # print(test_get_text)
    return render(request, 'reverse.html', {})