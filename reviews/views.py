from django.shortcuts import render

# Create your views here.
def all_reviews(request):
    """Redners all reviews"""
    return render(request, 'reviews/all-reviews.html')