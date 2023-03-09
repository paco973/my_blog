from django.shortcuts import render, redirect, reverse
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import login
from user_profile.models.user import User

from user_profile.forms.sign_up_form import SignupForm


# Create your views here.
class SignupView(View):
    template_name = 'auth/signup.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse('index'))
        form = SignupForm()

        return render(request, self.template_name, {'form': form})

    def post(self, request):

        form = SignupForm(request.POST)

        if form.is_valid():

            # Do something with the form data
            user = User.objects.create_user(email=form.cleaned_data['email'], password=form.cleaned_data['password'],
                                            subscribe=form.cleaned_data['subscribe'])

            if user is not None:
                login(request, user)
                return HttpResponse('ok je me suis inscrit')

        form = SignupForm()
        return render(request, self.template_name, {'form': form})
