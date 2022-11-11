from django.db import models

# Create your models here.

class institution(models.Model):
    sname = models.CharField(max_length=50)
    course = models.CharField(max_length=40)
    fee = models.IntegerField()


class transport(models.Model):
    bus = models.IntegerField()
    plane = models.IntegerField()
    ola = models.IntegerField()
