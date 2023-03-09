from django import forms
from django.core.exceptions import ValidationError
from user_profile.models.user import User
from secrets import compare_digest


class SignupForm(forms.Form):
    email = forms.EmailField(label='Email address',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail',
                                                            'id': 'email'}))
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '*********',
                                                                 'id': 'password'}))
    password2 = forms.CharField(label='Confirm Password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '*********',
                                                                  'id': 'password2'}))
    subscribe = forms.BooleanField(label='Yes i\'d also like to sign up for additional subscription', required=False,
                                   widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'subscribe'}))

    class Meta:
        model = User
        fields = ['email', 'password']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError('This email address is already in use.')
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password and password2 and not compare_digest(password, password2):
            print(password, password2, compare_digest(password, password2))
            raise ValidationError('Passwords do not match.')
