from django.utils import timezone
from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=254, blank=True)
    create_data = models.DateTimeField(default=timezone.now)
    descrition = models.TextField(blank=True)