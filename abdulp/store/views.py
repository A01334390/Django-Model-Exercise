# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from .models import (
    Notebook,
    NotebookOrder,
    Client,
    Order,
    Page
)

# Create your views here.

# //////// Listing of models ////////
class NotebookList(ListView):
    model = Notebook

class ClientList(ListView):
    model = Client

#class OrderList(ListView):
#    model = Order

class PageList(ListView):
    model = Page

# //////// Creation of models ///////////
class NotebookCreation(CreateView):
    model = Notebook
    success_url = reverse_lazy('notebook_list')
    fields = ['nType','benefit']

class ClientCreation(CreateView):
    model = Client
    success_url = reverse_lazy('client_list')
    fields = ['firstName','secondName','address','isPhysical','email']

#class OrderCreation(CreateView):
#    model = 

class PageCreation(CreateView):
    model = Page,
    success_url = reverse_lazy('page_list')
    fields = ['description','cost']

# ////////// Update Viws ///////////
class NotebookUpdate(UpdateView):
    model = Notebook
    success_url = reverse_lazy('notebook_list')
    fields = ['nType','benefit']

class ClientUpdate(UpdateView):
    model = Client
    success_url = reverse_lazy('client_list')
    fields = ['firstName','secondName','address','isPhysical','email']

#class OrderCreation(CreateView):
#    model = 

class PageUpdate(UpdateView):
    model = Page,
    success_url = reverse_lazy('page_list')
    fields = ['description','cost']

# //////// Delete View //////////
class NotebookDelete(DeleteView):
    model = Notebook
    success_url = reverse_lazy('notebook_list')

class ClientDelete(DeleteView):
    model = Client
    success_url = reverse_lazy('client_list')

class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('page_list')

# //////// Detailed View /////////
class ClientDetail(DetailView):
    model = Client

class NotebookDetail(DetailView):
    model = Notebook

class PageDetail(DetailView):
    model = Page
