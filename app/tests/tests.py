import pytest
from django.test import TestCase

from app.models import Category

class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='test_category')

    def test_category_name(self):
        category = Category.objects.get(id=1)
        expected_name = f'{category.name}'
        self.assertEquals(expected_name, str(category))

    @pytest.mark.django_db
    def test_category_absolute_url(self):
        category = Category.objects.get(id=1)
        self.assertEquals(category.slug, 'test_category')