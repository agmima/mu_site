from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, ListView, DetailView, UpdateView,DeleteView
from .models import Post

class CreatePost(CreateView):
    model = Post
    fields = '__all__'
    template_name = 'create_post.html'
    success_url = '/'

class ListPost(ListView):
    model = Post
    template_name = 'post.html'
    success_url = '/'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    success_url = '/'

class EditPost(UpdateView):
    model = Post
    fields = '__all__'
    template_name = 'post_edit.html'
    success_url = '/'

class DeletePost(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = '/'






# Create your views here.
