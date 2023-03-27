from django.shortcuts import render, redirect
from django.views import View

from dashboard.forms.profile_form import ProfileForm


class UserView(View):
    template_name = 'dashboard/user/index.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('post')

        form = ProfileForm(instance=request.user)

        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('post')

        form = ProfileForm( request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()

            return redirect('post')

        context = {
                'form': form
            }
        return render(request, self.template_name, context)
