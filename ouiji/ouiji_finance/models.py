from __future__ import unicode_literals

from django.db import models
from datetime import date
import django

# Create your models here.

class Quote(models.Model):
	symbol = models.CharField(max_length=100, blank=False, default='')
	today = models.DateField(default=django.utils.timezone.now)