# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Plural(models.Model):
    edition = models.DateField()
    position = models.SmallIntegerField()
    headline = models.CharField(max_length = 140)
    text = models.TextField()
    link = models.URLField()
    hattips = models.URLField()