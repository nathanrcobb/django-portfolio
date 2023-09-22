from django.shortcuts import render
from .models import Project


def handler404(request, exception=None):
  if exception:
    print("*** 404 exception encountered: ", exception, "\n")

  response = render(request, "404.html")
  response.status_code = 404
  return response


def handler500(request, exception=None):
  if exception:
    print("*** 500 exception encountered: ", exception, "\n")

  response = render(request, "500.html")
  response.status_code = 500
  return response


def home(request):
  projects = Project.objects.all()

  return render(request, 'portfolio/home.html', {
    'projects': projects
  })
