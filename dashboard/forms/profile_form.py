from django import forms
from user_profile.models.user import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'location', 'bio', 'birthday', 'photo']

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}))
    username = forms.CharField(label='Username',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'value': 'webestica.com'}))
    location = forms.CharField(label='Location', widget=forms.TextInput(attrs={'class': 'form-control'}))
    bio = forms.CharField(label='Bio', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}))
    birthday = forms.DateField(
        widget=forms.TextInput(attrs={'class': 'form-control flatpickr-input', 'placeholder': 'DD/MM/YYYY'}))
    photo = forms.ImageField(label='Profile picture', widget=forms.FileInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'First name'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Last name'})
