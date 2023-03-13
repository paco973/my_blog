from django.shortcuts import render,get_object_or_404
from django.views import View
from app.models import Post
from app.models.category import Category


# Create your views here.
class PostView(View):
    template_name = 'post/index.html'

    def get(self, request, id=None):
        if not id:
            posts = Post.objects.all()
            categories = Category.objects.all()

            context = {
                'posts': posts,
                'categories': categories
            }
            return render(request, self.template_name,context )

        post = get_object_or_404(Post, id=id)

        context = {
            'post': post,
        }
        return render(request, 'post/post_detail.html', context)
