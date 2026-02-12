from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('description',)
        widgets = {
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,  # make it smaller
                'placeholder': 'Write your comment...'
            })
        }