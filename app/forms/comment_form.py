from django import forms
from app.models import Comment
from django.utils.text import gettext_lazy as _


class CommentForm(forms.ModelForm):

    body = forms.CharField(label=_('Comment'), widget=forms.Textarea(attrs={'class':'form-control', 'row':'3'}))
    class Meta:
        model = Comment
        fields = ['body']
