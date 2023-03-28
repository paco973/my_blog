from django.shortcuts import render, get_object_or_404
from django.views import View

from app.forms.comment_form import CommentForm
from app.models import Post, Category, Comment, PostView as pv
from django.db.models import Q


def _view_id(request):
    view_id = request.session.session_key
    if not view_id:
        view_id = request.session.create()
    return view_id


def related_posts( post):
    related_posts = Post.objects.get_published_post() \
                        .filter(Q(tag__in=post.tag.all()) | Q(category=post.category)) \
                        .exclude(id=post.id) \
                        .distinct() \
                        .order_by('-created_at')[:5]

    return related_posts


class PostView(View):
    template_name = 'post/index.html'

    def get(self, request, slug=None):

        if not slug:
            # Get all posts and categories
            query = request.GET.get('q')

            qs = Post.objects.get_published_post(query=query)
            categories = Category.objects.all()
            recommended_posts = self.recommended_posts(request)
            context = {
                'posts': qs,
                'categories': categories,
                'recommended_posts': recommended_posts
            }
            return render(request, self.template_name, context)

        # Get the post and its related posts
        post = get_object_or_404(Post, slug=slug)

        # Get the view object for the current user and post

        if request.user.is_authenticated:
            view = pv.objects.filter(post=post, key=_view_id(request), user=None)
            user_view = pv.objects.filter(post=post, user=request.user).exists()
            if view.count() > 0 and not user_view:
                try:
                    view[0].user = request.user
                    view[0].save()
                except:
                    print('ça existe déjà')
            elif not user_view:
                try:
                    view = pv.objects.create(key=_view_id(request), user=request.user, post=post)
                    view.save()
                except:
                    print('ça existe déjà')
        else:
            view = pv.objects.filter(post=post, key=_view_id(request))
            if view.count() == 0:
                view = pv.objects.create(key=_view_id(request), post=post)
                view.save()

        preview = Post.objects.get_published_post().filter(published_date__lt=post.published_date).first()
        next = Post.objects.get_published_post().filter(published_date__gt=post.published_date).last()
        comments = Comment.objects.filter(post=post)
        comment_form = CommentForm()

        context = {
            'post': post,
            'related_posts': related_posts(post),
            'next': next,
            'preview': preview,
            'comments': comments,
            'comment_form': comment_form
        }
        return render(request, 'post/post_detail.html', context)

    def recommended_posts(self, request):
        user = request.user

        if not user.is_authenticated:
            viewed_posts = pv.objects.filter(key=_view_id(request)).values_list('post', flat=True)
        else:
            viewed_posts = pv.objects.filter(key=_view_id(request), user=user).values_list('post', flat=True)

        tags = Post.objects.get_published_post().filter(pk__in=viewed_posts).values_list('tag', flat=True)
        categories = Post.objects.get_published_post().filter(pk__in=viewed_posts).values_list('category', flat=True)

        related_posts = Post.objects.get_published_post().filter(Q(tag__in=tags) | Q(category__in=categories)) \
                            .exclude(id__in=viewed_posts) \
                            .distinct() \
                            .order_by('-created_at')[:5]
        return related_posts
