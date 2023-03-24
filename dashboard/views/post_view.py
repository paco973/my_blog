from django.shortcuts import render, redirect
from django.views import View
from dashboard.forms.post_form import PostForm


class PostView(View):
    template_name = 'dashboard/post/index.html'

    def get(self, request):

        form = PostForm()


        context = {
            'form': form
        }

        return render(request, self.template_name, context)

    def post(self, request):
        form = PostForm(request.POST, request.FILES)
       
        if form.is_valid():
            print('oaddikjidwdiji')
            form.save()
            context = {
                'form': form
            }
            return render(request, self.template_name, context)

        context = {
            'form': form
        }

        return render(request, self.template_name, context)

 
