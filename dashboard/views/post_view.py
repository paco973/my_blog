from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponseBadRequest
from app.models import Post
from dashboard.forms.post_form import PostForm


class PostView(View):
    template_name = 'dashboard/post/index.html'

    def get(self, request, slug=None):

        if slug is None:
            url = None
            form = PostForm()
        else:
            post = Post.objects.get(slug=slug)
            url = post.get_edit_url()
            form = PostForm(instance=post)

        context = {
            'form': form,
            'url': url
        }

        return render(request, self.template_name, context)

    def post(self, request, slug=None):

        if slug is None:
            url = None
            form = PostForm(request.POST, request.FILES)
        else:
            post = get_object_or_404(Post, slug=slug)
            url = post.get_edit_url()
            form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

        context = {
            'form': form,
            'url': url
        }

        return render(request, self.template_name, context)



def delete_post(request, id):
    post = get_object_or_404(Post, id=id)

    try:
        post.delete()
    except Exception:
        return HttpResponseBadRequest(status=400)

    return redirect('dashboard')