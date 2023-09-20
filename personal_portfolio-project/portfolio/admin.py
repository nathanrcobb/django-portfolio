from django.contrib import admin
from .models import Project, Tech, TechUsage
from blog.models import Blog

admin.site.register(Project)
admin.site.register(Tech)
admin.site.register(TechUsage)
admin.site.register(Blog)
