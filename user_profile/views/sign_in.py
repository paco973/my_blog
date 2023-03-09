from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

from user_profile.forms.sign_in_form import SignInForm


# Create your views here.
class SigninView(View):
    template_name = 'auth/signin.html'

    def get(self, request):
        form = SignInForm()

        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SignInForm(request.POST)
        if form.is_valid():
            # Do something with the form data
            print()
            user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return HttpResponse('ok')

        form = SignInForm()
        return render(request, self.template_name, {'form': form})
