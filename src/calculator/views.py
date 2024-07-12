from django.shortcuts import render

# Create your views here.

def calculator_page_view(request):
    return render(request, 'calculator/main_calculator.html', {})