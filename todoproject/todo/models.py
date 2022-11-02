from django.db import models

# Create your models here.
class task(models.Model):
    heading=models.CharField(max_length=20)
    deatils=models.CharField(max_length=20)
    date=models.DateField()
    is_deleted=models.CharField(max_length=2)
