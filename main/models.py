from django.db import models

# Create your models here.
class Post(models.Model):
    # post = models.CharField(max_length=500)
    destination_name = models.CharField(max_length=20)
    # user = models.ForeignKey(User)
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)
