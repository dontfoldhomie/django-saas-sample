from django.db import models

# Create your models here.

class Student(models.Model):
    your_name = models.CharField(max_length=100)
    your_email =models.EmailField()
    your_school = models.CharField()
    your_major = models.CharField()
    your_living_choice = models.CharField()
    your_financial_assistance = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
