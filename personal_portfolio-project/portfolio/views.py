from django.shortcuts import render
from .models import Project


def handler404(request, exception=None):
  response = render(request, "404.html", {
      "exception": exception
    })
  response.status_code = 404
  return response


def handler500(request, exception=None):
  response = render(request, "500.html", {
      "exception": exception
    })
  response.status_code = 500
  return response


def home(request):
  projects = Project.objects.all()

  return render(request, 'portfolio/home.html', {
    'projects': projects
  })
