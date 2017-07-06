from django.db import models


# Create your models here.
class Item(models.Model):
    # I want attribute 'text' to be a text field in the database, and be taken into account for persistence
    text = models.TextField(default='')
