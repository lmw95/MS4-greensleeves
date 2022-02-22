from django import forms
from blog.models import Comment


class CommentForm(forms.ModelForm):
    """Creates instance of comment form"""
    class Meta:
        """Provides field for comment form"""
        model = Comment
        fields = ['comment']
