from django.test import TestCase
from django.urls import reverse

from app.models import Category, Post


class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Créer des objets de modèle pour les tests
        Category.objects.create(name='Test category', color='red')

    def test_name_field(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('name').max_length
        self.assertEquals(max_length, 255)

    def test_color_field(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('color').max_length
        self.assertEquals(max_length, 50)

    def test_str_method(self):
        category = Category.objects.get(id=1)
        self.assertEquals(str(category), 'Test category')

    def test_posts_property(self):
        # Créer un objet Post associé à une catégorie
        post = Post.objects.create(
            title='Test post',
            content='Test content',
            status='published',
            category_id=1
        )

        # Vérifier que la propriété posts renvoie le bon résultat
        category = Category.objects.get(id=1)
        posts = category.posts
        self.assertEquals(len(posts), 1)
        self.assertEquals(posts[0].title, 'Test post')

    def test_absolute_url_method(self):
        category = Category.objects.get(id=1)
        url = reverse('category', kwargs={'slug': category.slug})
        self.assertEquals(url, '/category/test-category/')
