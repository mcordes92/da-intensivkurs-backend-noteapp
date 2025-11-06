from django.db import models

# Create your models here.
class notes(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    marked = models.BooleanField(default=False)
    trash = models.BooleanField(default=False)