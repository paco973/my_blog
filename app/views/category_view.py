from django.shortcuts import render, get_object_or_404
from django.views import View
from app.models import Category


class CategoryView(View):
    template_name = 'category/index.html'

    def get(self, request, id):

        category = get_object_or_404(Category, id=id)
        categories = Category.objects.all().exclude(id=category.id)
        context = {
            'categories': categories,
            'category': category
        }
        return render(request, self.template_name, context)
