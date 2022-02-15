from django.shortcuts import render

# Create your views here.
def blog(request):
    """Renders the blog page"""
    return render(request, 'blog/blog.html')