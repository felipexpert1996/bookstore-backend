from rest_framework.serializers import ModelSerializer
from .models import Category, Author, Book


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AuthorSerializer(ModelSerializer):
    category = CategorySerializer(many=True, read_only=False, required=False, help_text='Categoria do autor')
    class Meta:
        model = Author
        fields = '__all__'

    def crete_categories(self, categories, author):
        for category in categories:
            category = Category.objects.create(**category)
            author.category.add(category)

    def create(self, validated_data):
        category = validated_data['category']
        del validated_data['category']
        author = Author.objects.create(**validated_data)
        self.crete_categories(category, author)
        return author


class AuthorAlternativeSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

    def update(self, instance, validated_data):
        author = Author.objects.get(pk=instance.pk)
        author.name = validated_data['name']
        author.save()
        return author
    

class BookSerializer(ModelSerializer):
    author = AuthorSerializer(many=False, required=False, help_text='Autor do livro')
    category = CategorySerializer(many=True, required=False, help_text='Categoria do livro')
    class Meta:
        model = Book
        fields = '__all__'

    def crete_categories(self, categories, obj):
        for category in categories:
            category = Category.objects.create(**category)
            obj.category.add(category)

    def create_author(self, author):
        category = author['category']
        del author['category']
        author = Author.objects.create(**author)
        self.crete_categories(category, author)
        return author

    def create(self, validated_data):
        category = validated_data['category']
        del validated_data['category']
        author = validated_data['author']
        del validated_data['author']
        author = self.create_author(author)
        book = Book.objects.create(**validated_data)
        book.author = author
        book.save()
        self.crete_categories(category, book)
        return book

    def update(self, instance, validated_data):
        if validated_data.get('category'):
            del validated_data['category']
        if validated_data.get('author'):
            del validated_data['author']
        book = Book.objects.get(pk=instance.pk)
        book.name = validated_data['name']
        book.price = validated_data['price']
        book.save()
        return book
