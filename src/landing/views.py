from django.shortcuts import render

# Create your views here.
from visits.models import PageVisit

def landing_page_view(request):
    qs = PageVisit.objects.all()
    PageVisit.objects.create(path=request.path)
    return render(request, "landing/main.html", {"page_view_count": qs.count()})