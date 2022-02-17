from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from profiles.models import UserProfile
from .forms import CommentForm

# Create your views here.
def blog(request):
    """Renders the blog page"""
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'blog/blog.html', context)


@login_required
def blog_page(request, slug):
    """Renders blog page details"""
    post = Post.objects.get(slug=slug)
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user_profile = user_profile
            comment.save()

            messages.success(request, 'Your comment was posted!')
            return redirect('blog_page', slug=post.slug)
    
    else:
        form = CommentForm

    context = {
        'post': post,
        'form': form,
        'user_profile': user_profile,
    }

    return render(request, 'blog/blog-page.html', context)
