from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from .models import Author, Book, Category


class AuthorTests(APITestCase):

    client = APIClient()
    pk=-1

    def create(self):
        url = reverse('author-list')
        data = {'name': 'Teste de autor', 'description':'teste unitário', 'category':[{
            'name': 'Teste de autor', 'description':'teste unitário'
        }]}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.pk = Author.objects.last().pk

    def update(self):
        url = reverse('author-detail', kwargs={'pk':self.pk})
        data = {'name': 'Teste de update', 'description':'teste unitário de atualizacao'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Author.objects.get(pk=self.pk).name, 'Teste de update')

    def detail(self):
        url = reverse('author-detail', kwargs={'pk':self.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.pk)

    def list(self):
        url = reverse('author-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.data[-1]['id'], self.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def delete(self):
        url = reverse('author-detail', kwargs={'pk':self.pk})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

teste = AuthorTests()
teste.create()
teste.update()
teste.detail()
teste.list()
teste.delete()


class BookTests(APITestCase):

    client = APIClient()
    pk=-1

    def create(self):
        url = reverse('book-list')
        data = {
            "author": {
                "category": [{
                    "name": "teste",
                    "description": "teste"
                }],
                "name": "teste"
            },
            "category": [{
                "name": "teste",
                "description": "teste"
            }],
            "name": "teste",
            "price": 10.20
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.pk = Book.objects.last().pk

    def update(self):
        url = reverse('book-detail', kwargs={'pk':self.pk})
        data = {'name': 'Teste de update', 'price':10.50}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get(pk=self.pk).name, 'Teste de update')

    def detail(self):
        url = reverse('book-detail', kwargs={'pk':self.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.pk)

    def list(self):
        url = reverse('book-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.data[-1]['id'], self.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def delete(self):
        url = reverse('book-detail', kwargs={'pk':self.pk})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)



teste = BookTests()
teste.create()
teste.update()
teste.detail()
teste.list()
teste.delete()


class CategoryTests(APITestCase):

    client = APIClient()
    pk=-1

    def create(self):
        url = reverse('category-list')
        data = {'name': 'Teste', 'description':'teste unitário'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.pk = Category.objects.last().pk

    def update(self):
        url = reverse('category-detail', kwargs={'pk':self.pk})
        data = {'name': 'Teste de update', 'description':'teste unitário de atualizacao'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Category.objects.get(pk=self.pk).name, 'Teste de update')

    def detail(self):
        url = reverse('category-detail', kwargs={'pk':self.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
                            response.data,
                             {
                                 'id': self.pk,
                                 'name': 'Teste de update',
                                 'description':'teste unitário de atualizacao'
                             }
                         )

    def delete(self):
        url = reverse('category-detail', kwargs={'pk':self.pk})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def list(self):
        url = reverse('category-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[-1], {
            'id': self.pk,
            'name': 'Teste de update',
            'description':'teste unitário de atualizacao'
        })


teste = CategoryTests()
teste.create()
teste.update()
teste.detail()
teste.list()
teste.delete()