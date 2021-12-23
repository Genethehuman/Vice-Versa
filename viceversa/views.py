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
    user_text = request.GET['usertext']
    print(user_text)
    reversed_slovo = ''
    slovo = user_text
    for i in range(len(slovo) - 1, -1, -1):
        reversed_slovo= reversed_slovo + slovo[i]
    print(reversed_slovo)
    return render(request, 'reverse.html', {'reversedslovo':reversed_slovo, 'usertext':user_text})