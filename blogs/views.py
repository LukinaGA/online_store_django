from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView

from blogs.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ("title", "content", "image", "publication_sign")


class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ("title", "content", "image", "publication_sign")


class BlogDeleteView(DeleteView):
    model = Blog


