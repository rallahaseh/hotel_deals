from django.db import models

# Create your models here.
class Post(models.Model):
    destination_name = models.CharField(max_length=20)
