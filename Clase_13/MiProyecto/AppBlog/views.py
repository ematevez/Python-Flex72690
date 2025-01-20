from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class PostListView( LoginRequiredMixin,ListView):
    model = Post
    template_name = 'AppBlog/post_list.html'
    context_object_name = 'posts'
       

class PostDetailView(LoginRequiredMixin, DetailView ):
    model = Post
    template_name = 'AppBlog/post_detail.html'
    
class PostCreateView(LoginRequiredMixin, CreateView):
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
    template_name = 'AppBlog/post_delete.html'
    success_url = reverse_lazy('index')

