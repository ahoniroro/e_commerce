from django.test import TestCase

from store.models import category, product
from django.contrib.auth.models import User

class TestcategoriesModel(TestCase):

    def setUp(self):
        self.data1 = category.objects.create(name='django', slug='django')

    def test_category_model_entry(self):
        """
        test category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, category))


    def test_category_model_entry(self):
        """
        test category model defualt name
        """
        data = self.data1
        self.assertEqual(str(data), 'django')

class TestproductsModel(TestCase):
    def setUp(self):
        category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        self.data1 = product.objects.create(category_id=1, title='django', created_by_id=1, slug='django', price='20.00', image='django')

    def test_products_model_entry(self):
        """
        test product model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, product))
        self.assertEqual(str(data), 'django')
