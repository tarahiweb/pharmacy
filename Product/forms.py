from django import forms
from .models import Comment,ChildComment



class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields = ['body','drug_slug']

class ChildCommentForm(forms.ModelForm):
    class Meta:
        model=ChildComment
        fields = ['body','drug_slug']