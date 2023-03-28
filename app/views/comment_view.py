from django.shortcuts import redirect, get_object_or_404
from django.views import View

from app.forms.comment_form import CommentForm
from app.models import Comment, Post


class CommentView(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        form = CommentForm(request.POST)
        form.is_valid()
        Comment.objects.create(user=request.user, post=post, body=form.cleaned_data['body'])

        return redirect( 'post_detail',  post.slug)

