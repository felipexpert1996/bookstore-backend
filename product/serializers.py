from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError
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
            category, created = Category.objects.get_or_create(**category)
            author.category.add(category)

    def create(self, validated_data):
        if validated_data.get('category'):
            category = validated_data['category']
            del validated_data['category']
        else:
            raise ValidationError(detail={"category": "This field is required."})
        author, created = Author.objects.get_or_create(**validated_data)
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
            category, created = Category.objects.get_or_create(**category)
            obj.category.add(category)

    def create_author(self, author):
        if author.get('category'):
            category = author['category']
            del author['category']
        else:
            raise ValidationError(detail={"category": "This field is required."})
        author, created = Author.objects.get_or_create(**author)
        self.crete_categories(category, author)
        return author

    def create(self, validated_data):
        if validated_data.get('category'):
            category = validated_data['category']
            del validated_data['category']
        else:
            raise ValidationError(detail={"category": "This field is required."})
        if validated_data.get('author'):
            author = validated_data['author']
            del validated_data['author']
        else:
            raise ValidationError(detail={"author": "This field is required."})
        author = self.create_author(author)
        book, created = Book.objects.get_or_create(**validated_data)
        book.author = author
        if validated_data.get('isHighlight'):
            book.isHighlight = True
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
        if validated_data['isHighlight']:
            book.isHighlight = True
        book.save()
        return book
