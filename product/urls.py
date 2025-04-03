from rest_framework.routers import DefaultRouter
from .views import CategoryViewset, AuthorViewset, BookViewset
from django.urls import path, include

router = DefaultRouter()
router.register(r'categories', CategoryViewset, basename='category')
router.register(r'authors', AuthorViewset, basename='author')
router.register(r'books', BookViewset, basename='book')


urlpatterns = [
    path('products/', include(router.urls)),
]