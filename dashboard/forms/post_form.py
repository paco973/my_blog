from django import forms
from app.models.post import Post
from app.models.category import Category
from app.models.tag import Tag
from django_quill.fields import QuillFormField

class PostForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    tag = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.SelectMultiple(attrs={'class': 'form-select'}))
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post name'}))
    body = QuillFormField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add description'}))
    image = forms.ImageField(label='Profile picture', widget=forms.FileInput(attrs={'class': 'form-control'}),required=False)

    class Meta:
        model = Post
        fields = ['category', 'tag', 'title', 'body', 'description', 'image']
