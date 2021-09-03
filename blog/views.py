from django.shortcuts import render, get_object_or_404
from .models import Blog
from .forms import CommentForm


#view for all blogs page
def all_blogs(request):
    # Total records count
    blog_count = Blog.objects.count()
    # Send maximum 5 last records to page
    blogs = Blog.objects.order_by('-date')[:5]
    return render(request, 'blog/all_blogs.html', {'blogs' : blogs, 'blog_count' : blog_count})

#detail blog with comments system
def detail(request, blog_id):
    template_name = 'blog/detail.html'
    blog = get_object_or_404(Blog, pk=blog_id)
    comments = blog.comments.all()

    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.blog = blog
            # Save the comment to the database
            new_comment.save()

    return render(request, template_name, {'blog': blog,
                                           'comments': comments,
                                           'comment_form': CommentForm()})
