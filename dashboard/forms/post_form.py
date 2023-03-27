from django import forms
from app.models import Category, Tag
from app.models.post import STATUS, Post
from django.utils.text import gettext_lazy as _


class PostForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(
        attrs={'class': 'form-select'}),required=True)
    tag = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.SelectMultiple(
        attrs={'class': 'form-select'}), required=True)
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post name'}), required=True)
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                                'placeholder': 'Add description'}), required=True)
    image = forms.ImageField(label=_('Post picture'), widget=forms.FileInput(attrs={'class': 'form-control'}),
                             required=True)

    status = forms.ChoiceField(label=_('Status'), choices=STATUS.choices, widget=forms.Select(attrs={'class': 'form-control'}))

    published_date = forms.DateTimeField(label=_('Date de publication'),required=False, widget=forms.DateTimeInput(attrs={'class':'form-control', 'type': 'datetime-local'}) )

    class Meta:
        model = Post
        fields = ['category', 'tag', 'title', 'body', 'description', 'image', 'status', 'published_date']
