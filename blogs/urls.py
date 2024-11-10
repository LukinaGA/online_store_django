from django.urls import path

from blogs.apps import BlogsConfig
from blogs.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView


app_name = BlogsConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('blogs/new/', BlogCreateView.as_view(), name='blog_create'),
    path('blogs/blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blogs/update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blogs/delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
]
