from django.shortcuts import render

# Create your views here.
from petAPP.models import *
from django.views.generic import ListView,DetailView,UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy 
class petList(ListView):
    model=petstore

class petdetails(DetailView):
    model=petstore

class updateView(UpdateView):
    model=petstore
    fields='__all__'

class deleteView(DeleteView):
    model=petstore
    success_url=reverse_lazy('list')

class createView(CreateView):
    model=petstore
    # fields=('title','auth_name','nopages','price')
    fields='__all__'