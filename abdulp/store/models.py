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

    def __unicode__(self):
        return self.firstName

class Order(models.Model):
    date = models.DateField()
    PRIORITY = (
        ('H','High'),
        ('N','Normal'),
        ('L','Low')
    )
    priority = models.CharField(
        choices = PRIORITY,
        max_length = 1,
        default = 'L',
    )
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE
    )
    def __unicode__(self):
        return str(self.id)

class Page(models.Model):
    description = models.CharField(max_length=40)
    cost = models.IntegerField()
    def __unicode__(self):
        return self.description
    
class Notebook(models.Model):
    nType = models.CharField(
        max_length = 50
    )
    benefit = models.IntegerField()
    def __unicode__(self):
        return self.nType

class NotebookOrder(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
    )
    quantity = models.PositiveIntegerField()
    notebook = models.ForeignKey(
        Notebook,
        on_delete=models.DO_NOTHING
    )
    STATUS = (
        ("NS","Not Started"),
        ("PP","Preparing..."),
        ("DO","Done"),
        ("SH","Shipping..."),
        ("SD","Shipped")
    )
    status = models.CharField(
        choices = STATUS,
        max_length = 2,
        default = "NS",
    )
    page = models.ForeignKey(
        Page,
        on_delete=models.DO_NOTHING
    )


