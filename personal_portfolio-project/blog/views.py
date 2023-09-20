from django.shortcuts import render, get_object_or_404
from .models import Blog


def all(request):
  blogs = Blog.objects.order_by('-date')

  # TODO: Deal with pagination

  return render(request, 'blog/all.html', {
    'blogs': blogs
  })


def detail(request, blog_id):
  blog = get_object_or_404(Blog, pk=blog_id)

  return render(request, 'blog/detail.html', {
    'blog': blog
  })
