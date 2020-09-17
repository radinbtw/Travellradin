from django.db import models

class travel_mdl(models.Model):
    name=models.CharField(max_length=30)
    origin=models.CharField(max_length=30)
    destination=models.CharField(max_length=30)
    date=models.DateField()
    time=models.TimeField()
