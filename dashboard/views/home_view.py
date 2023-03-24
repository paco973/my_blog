from django.shortcuts import render, redirect
from django.views import View
from app.models import Post


class HomeView(View):
    template_name = 'dashboard/home/index.html'

    def get(self, request):
        user = request.user

        if not user.is_staff:
            return redirect('user')

        if user.is_superuser:
            posts = Post.objects.all()
        else:
            posts = Post.objects.filter(user=user)

        last_posts = Post.objects.all()[:5]

        context = {
            'last_posts': last_posts,
            'posts': posts
        }

        return render(request, self.template_name, context=context)

