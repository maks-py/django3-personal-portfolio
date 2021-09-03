"""Views for portfolio app"""
from django.shortcuts import render

from .models import Project


def home(request):
    """Homepage render"""
    proj = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':proj})
