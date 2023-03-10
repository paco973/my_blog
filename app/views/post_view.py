from django.shortcuts import render
from django.views import View

from app.models import Post
from app.models.category import Category


# Create your views here.
class PostView(View):
    template_name = 'post/index.html'

    def get(self, request):
        posts = Post.objects.all()
        categories = Category.objects.all()

        context = {
            'posts': posts,
            'categories': categories
        }
        return render(request, self.template_name,context )
