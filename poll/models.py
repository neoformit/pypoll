from django.db import models

# Create your models here.
class Poll(models.Model):
    name = models.CharField(max_length=50)
    comment = models.TextField(max_length=1500)
    date = models.DateField(auto_now_add=True)
