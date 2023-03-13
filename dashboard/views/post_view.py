from django.shortcuts import render, redirect
from django.views import View
from ..forms.post_form import QuillFieldForm


class PostView(View):
    template_name = 'dashboard/post/index.html'

    def get(self, request):
        request.user.is_authenticated
        form = QuillFieldForm()

        context = {
            'form': form
        }

        return render(request, self.template_name, context)
