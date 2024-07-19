from django.shortcuts import render
from django.http import HttpResponse
from .models import StudentForm
from django.http import HttpResponseRedirect

# Create your views here.
def calculator_page_view(request, *args, **kwargs):
    form = StudentForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        calculator_object = form.save()
        context['object'] = calculator_object
        context['created'] = True
        return HttpResponseRedirect("/")

    return render(request, "calculator/main.html", context=context)