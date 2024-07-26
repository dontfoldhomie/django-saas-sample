from django.db import models
from django.forms import ModelForm
from django import forms

# Create your models here.


UNIVERSITY_CHOICES = {
    "UCLA": "ucla",
    "UCSD": "ucsd",
    "UCI": "uci",
}

MAJOR_CHOICES = {
    "Business": "business",
    "Computer Science": "computer science",
}


class Student(models.Model):
    name = models.CharField(max_length=100,)
    university = models.CharField(max_length=100, choices=UNIVERSITY_CHOICES,)
    email = models.EmailField(max_length=100,)
    major = models.CharField(max_length=100, choices=MAJOR_CHOICES,)
    yearly_tuition = models.DecimalField(max_digits=6, decimal_places=2)
    financial_assistance = models.DecimalField(max_digits=6, decimal_places=2)
    years_in_school = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name




class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ["name", "email", "university", "major", "yearly_tuition", "financial_assistance", "years_in_school"]


