# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import (
    Notebook,
    NotebookOrder,
    Client,
    Order,
    Page
)
# Register your models here.
admin.site.register(
    Notebook
)
admin.site.register(
    NotebookOrder
)
admin.site.register(
    Client
)
admin.site.register(
    Order
)
admin.site.register(
    Page
)