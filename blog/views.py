from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy


class BlogListView(ListView):
    model = Post
    template_name = 'blog_list.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog_new.html'
    fields = ['title', 'author', 'body']


class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title', 'body']
    template_name = 'blog_edit.html'


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('blog_list')
