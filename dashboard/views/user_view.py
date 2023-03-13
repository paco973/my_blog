from django.shortcuts import render
from django.views import View

from dashboard.forms.profile_form import ProfileForm


class UserView(View):
    template_name = 'dashboard/user/index.html'

    def get(self, request):
        form = ProfileForm()
        form.ob
        context = {
            'form':form
        }
        return render(request, self.template_name, context)

    def put(self, request):
        form = ProfileForm(request.PUT)
        context = {
            'form': form
        }
        return render(request, self.template_name, context)