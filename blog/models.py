from django.db import models
from profiles.models import UserProfile


class Post(models.Model):
    """Creates instance of a post"""
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    image = models.ImageField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Sorts posts by newest first"""
        ordering = ['date_added']


class Comment(models.Model):
    """Creates instance of comment"""
    post = models.ForeignKey(
        Post, related_name="comments", on_delete=models.CASCADE)
    user_profile = models.ForeignKey(
        UserProfile, null=False, blank=False, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Sorts comments by newest first"""
        ordering = ['-date_added']
