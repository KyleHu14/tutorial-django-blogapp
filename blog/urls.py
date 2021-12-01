from django.urls import path, include
from .views import BlogListView, BlogDetailView

urlpatterns = [
    path('', BlogListView.as_view(), name = 'blog-home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name = 'post-detail'),
]