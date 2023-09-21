from django.db import models


class Project(models.Model):
  title = models.CharField(max_length=100)
  description = models.CharField(max_length=250)
  image = models.ImageField(upload_to='images/projects/')
  url = models.URLField(blank=True)
  position = models.IntegerField(blank=True)

  def __str__(self):
    return self.title


class Tech(models.Model):
  name = models.CharField(max_length=40)

  def __str__(self):
    return self.name


class TechUsage(models.Model):
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  tech = models.ForeignKey(Tech, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.project.title} - {self.tech.name}"
