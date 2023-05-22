from django.db import models

# Create your models here.
class Hydjobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=100)
    title=models.CharField(max_length=30)
    elegiblity=models.CharField(max_length=30)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    phonenumber=models.BigIntegerField()
class Punejobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=100)
    title=models.CharField(max_length=30)
    elegiblity=models.CharField(max_length=30)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    phonenumber=models.BigIntegerField()
class Bngjobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=100)
    title=models.CharField(max_length=30)
    elegiblity=models.CharField(max_length=30)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    phonenumber=models.BigIntegerField()
