from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import CalculatorForm
# Create your views here.

def calculator_page_view(request):
        # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = CalculatorForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/calculator/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CalculatorForm()
    return render(request, 'calculator/main_calculator.html', {"form": form})

def upload(request):
    render(request, 'calculator.upload.html')