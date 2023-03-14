from django.shortcuts import render,get_object_or_404
from django.views import View
from app.models import Post
from app.models.category import Category
from app.models.post_like import PostLike
from app.models.post_view import PostView as pv


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


        related_post =[] #self.recommended_posts()
        post = get_object_or_404(Post, id=id)

        context = {
            'post': post,
            'related_post': related_post
        }
        return render(request, 'post/post_detail.html', context)

    def recommended_posts(request):
        user = request.user
        if not user.is_authenticated:
            # If the user is not logged in, return an empty list
            return []
        # Get the user's previously viewed and liked posts
        viewed_posts = pv.objects.filter(user=user).values_list('post', flat=True)
        liked_posts = PostLike.objects.filter(user=user).values_list('post', flat=True)
        # Get a list of tags that the user is interested in
        tags = user.profile.tags.all()
        # Combine the previously viewed and liked posts and user's interested tags
        related_posts = Post.objects.filter(tag__in=tags) \
                            .exclude(id__in=viewed_posts) \
                            .exclude(id__in=liked_posts) \
                            .distinct() \
                            .order_by('-created_at')[:5]
        return related_posts