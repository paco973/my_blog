from django.shortcuts import render, redirect, reverse
from django.views import View
from django.contrib.auth import authenticate, login
from django.conf import settings
from user_profile.forms.sign_in_form import SignInForm


class SigninView(View):
    template_name = 'auth/signin.html'

    def get(self, request):

        if request.user.is_authenticated:
            return redirect(reverse('index'))

        form = SignInForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SignInForm(request.POST)
        if form.is_valid():
            # Do something with the form data
            user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)

                if request.POST['keep_signed_in']:
                    settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = False
                else:
                    settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = True

                return redirect('post')

        form = SignInForm()
        return render(request, self.template_name, {'form': form})
