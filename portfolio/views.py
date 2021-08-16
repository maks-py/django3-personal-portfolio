from django.shortcuts import render
from .models import Project


def home(request):
  proj = Project.objects.all()
  return render(request, 'portfolio/home.html', {'projects':proj})