# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Client(models.Model):
    firstName = models.CharField(
        max_length = 80
    )
    secondName = models.CharField(
        max_length = 80
    )
    address = models.CharField(
        max_length = 80
    )
    isPhysical = models.BooleanField(
        default = True
    )
    email = models.EmailField(
        unique = True
    )

class Order(models.Model):
    date = models.DateField()
    priority = (
        'High',
        'Normal',
        'Low'
    )
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE
    )

class Page(models.Model):
    description = models.CharField(max_length=40)
    cost = models.PositiveSmallIntegerField()
    
class Notebook(models.Model):
    nType = models.CharField(
        max_length = 50
    )
    benefit = models.IntegerField()

class NotebookOrder(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        primary_key = True
    )
    quantity = models.PositiveIntegerField()
    notebook = models.ForeignKey(
        Notebook,
        on_delete=models.DO_NOTHING
    )
    status = (
        "Not Started",
        "Preparing...",
        "Done",
        "Shipping...",
        "Shipped"
    )
    page = models.OneToOneField(
        Page,
        on_delete=models.DO_NOTHING
    )


