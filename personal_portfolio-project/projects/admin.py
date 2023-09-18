from django.contrib import admin
from .models import Project, Tech, TechUsage

admin.site.register(Project)
admin.site.register(Tech)
admin.site.register(TechUsage)
