from django.shortcuts import render, redirect
from blog.models import Post
from .forms import CommentForm

# Create your views here.
def blog(request):
    """Renders the blog page"""
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'blog/blog.html', context)


def blog_page(request, slug):
    """Renders blog page details"""
    post = Post.objects.get(slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('blog_page', slug=post.slug)
    
    else:
        form = CommentForm

    context = {
        'post': post,
        'form': form,
    }

    return render(request, 'blog/blog-page.html', context)