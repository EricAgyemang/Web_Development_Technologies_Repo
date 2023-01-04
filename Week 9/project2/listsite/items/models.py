from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Item(models.Model):
    text = models.CharField(max_length=2000)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    #done = models.BooleanField(default=False)
