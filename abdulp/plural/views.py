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
from .models import Plural

class PluralList(ListView):
    model = Plural

class PluralDetail(DetailView):
    model = Plural

class PluralCreation(CreateView):
    model = Plural
    success_url = reverse_lazy('plural:list')
    fields = ['edition','position','headline','text','link','hattips']

class PluralUpdate(UpdateView):
    model = Plural
    success_url = reverse_lazy('plural:list')
    fields = ['edition','position','headline','text','link','hattips']

class PluralDelete(DeleteView):
    model = Plural
    success_url = reverse_lazy('plural:list')
# Create your views here.
