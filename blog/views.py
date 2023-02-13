from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post


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
