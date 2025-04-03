from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    name = models.CharField(max_length=200, help_text='Nome da categoria')
    description = models.TextField(help_text='Descrição da categoria')

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200, help_text='Nome do autor')
    category = models.ManyToManyField(Category, help_text='Categoria de livros do autor')

    def __str__(self):
        return self.name
    

class Book(models.Model):
    name = models.CharField(max_length=200, help_text='Nome do livro')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True, help_text='Autor do livro')
    category = models.ManyToManyField(Category, help_text='Categoria do livro')
    price = models.DecimalField(max_digits=14, decimal_places=2, validators=[MinValueValidator(0.10), MaxValueValidator(999999999999.00)], help_text='Preço do livro')

    def __str__(self):
        return self.name