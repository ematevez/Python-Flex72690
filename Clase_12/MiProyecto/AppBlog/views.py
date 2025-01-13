from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'AppBlog/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'AppBlog/post_detail.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'AppBlog/post_form.html'
    fields = ['title', 'content', 'author']
    success_url = reverse_lazy('post_list')

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'AppBlog/post_form.html'
    fields = ['title', 'content', 'author']
    success_url = reverse_lazy('post_list')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'AppBlog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')