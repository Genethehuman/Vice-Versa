from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_title, name='show_title'),

]