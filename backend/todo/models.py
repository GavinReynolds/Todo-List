from django.db import models

class Todo(models.Model):
    text = models.CharField(max_length=250)
    complete = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
