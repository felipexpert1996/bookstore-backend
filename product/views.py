from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Category, Author, Book
from .serializers import CategorySerializer, AuthorSerializer, AuthorAlternativeSerializer, BookSerializer


class CategoryViewset(ModelViewSet):

    """
   list:
   Retorna uma lista de categorias cadastradas

   create:
   Cria uma instancia de categoria

   delete:
   Deleta um categoria especifico

   read:
   Mostra detalhes da categoria

   update:
   Atualiza dados da categoria

   partial_update:
   Atualiza dados da categoria
   """


    model = Category
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class AuthorViewset(ModelViewSet):

    """
    list:
    Retorna uma lista de autores cadastrados

    create:
    Cria uma instancia de autor

    delete:
    Deleta um autor especifico

    read:
    Mostra detalhes do autor

    update:
    Atualiza dados do autor

    partial_update:
    Atualiza dados do autor

    get_nome:
    exemplo de extra action com parametro

    status:
    exemplo de extra action sem parametro
    """

    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

    @action(detail=True, methods=['get'])
    def get_nome(self, request, pk):
        return Response({'nome':f'{Author.objects.get(pk=pk).name}'})

    def get_serializer_class(self):
        actions = [
            'create',
            'list',
            'partial_update',
            'delete',
            'get_nome',
            'status'
        ]
        if self.action in actions:
            return AuthorAlternativeSerializer
        return self.serializer_class


class BookViewset(ModelViewSet):

    """
   list:
   Retorna uma lista de livros cadastrados

   create:
   Cria uma instancia de livro

   delete:
   Deleta um livro especifico

   read:
   Mostra detalhes do livro

   update:
   Atualiza dados do livro

   partial_update:
   Atualiza dados do livro
   """

    queryset = Book.objects.all()
    serializer_class = BookSerializer