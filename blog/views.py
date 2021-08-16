from django.shortcuts import render, get_object_or_404
from .models import Blog

#view for all blogs page
def all_blogs(request):
  # Total records count
  blog_count = Blog.objects.count()
  # Send maximum 5 last records to page
  blogs = Blog.objects.order_by('-date')[:5]
  return render(request, 'blog/all_blogs.html', {'blogs' : blogs, 'blog_count' : blog_count})

#view for blog detailed page
def detail(request, blog_id):
  blog = get_object_or_404(Blog, pk=blog_id)
  return render(request, 'blog/detail.html', {'blog' : blog})
