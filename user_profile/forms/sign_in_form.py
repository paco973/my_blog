from django import forms


class SignInForm(forms.Form):
    email = forms.EmailField(label='Email address', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'E-mail'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'id': 'password', 'placeholder': '*********'}))
    keep_signed_in = forms.BooleanField(label='Keep me signed in', required=False, widget=forms.CheckboxInput(
        attrs={'class': 'form-check-input', 'id': 'keep_signed_in'}))


