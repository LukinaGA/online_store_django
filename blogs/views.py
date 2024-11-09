from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView

from blogs.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ("title", "content", "image", "publication_sign")
    success_url = reverse_lazy('blog_list')


class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ("title", "content", "image", "publication_sign")
    success_url = reverse_lazy('blog_detail')


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog_list')
