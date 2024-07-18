from django import forms
from django.forms import ModelForm
from .models import Student

SCHOOL_CHOICES =( 
    ("1","UCLA"), 
    ("2","UCSD"), 
    ("3","SDSU"), 
    ("4","USD"), 
    ("5","USC"), 
) 

ROOM_CHOICE =(
    ("1", "Yes"),
    ("2", "No")
)

MAJOR_CHOICES =(
    ("1", "Information Systems"),
    ("2", "Computer Science"),
    ("3", "Business Management"),
    ("4", "Finance"),
    ("5", "Biology"),
    ("6", "Political Science"),
    ("7", "Psychology"),
    ("8", "Childhood Education"),
    ("9", "Sports Science"),
    ("10", "Math"),
)

ROOM_CHOICE =(
    ("1", "Yes"),
    ("1", "No"),
)

class CalculatorForm(ModelForm):
    your_name = forms.CharField(label="Your name", max_length=100)
    your_email =forms.EmailField(label="Your Email")
    your_school = forms.TypedChoiceField(choices=SCHOOL_CHOICES)
    your_major = forms.TypedChoiceField(choices=MAJOR_CHOICES)
    your_living_choice = forms.ChoiceField(label="Will you pay for room and board?", choices=ROOM_CHOICE)
    your_finacial_assistance = forms.IntegerField(label="External Financial Assistance? (Scholarship, Grants, etc)")

    class Meta:
        model = Student
        fields = ['your_name', 'your_email', 'your_school', 'your_major', 'your_living_choice', 'your_financial_assistance']