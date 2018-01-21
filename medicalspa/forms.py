from django import forms
from .models import Comment,ChildComment
from django import forms
from .models import Compound


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields = ['body','drug_slug']

class ChildCommentForm(forms.ModelForm):
    class Meta:
        model=ChildComment
        fields = ['body','drug_slug']


class CompoundCreateForm(forms.ModelForm):
    class Meta:
         model = Compound
         fields = ['Medical_spa_name', 'Phone_number', ]