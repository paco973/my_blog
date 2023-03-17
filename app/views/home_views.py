from django.shortcuts import render, redirect
from django.views import View

from app.models import Post
from app.models.category import Category


# Create your views here.
class HommeView(View):
    template_name = 'home/index.html'

    def get(self, request):

        return redirect('post')
        posts = Post.objects.all()
        categories = Category.objects.all()

        context = {
            'posts': posts,
            'categories': categories
        }
        return render(request, self.template_name,context )
