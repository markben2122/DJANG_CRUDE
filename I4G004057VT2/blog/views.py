from audioop import reverse
from django.shortcuts import render
from django.views import generic
from .models import Post
from django.urls import reverse_lazy
# Create your views here.
class PostDetailViews(generic.Datailview):
    model = Post 

class PostListViews(generic.ListView):
    model = Post
    fields= "__all__"
    success_url= reverse_lazy('blog:all')

class PostCreateViews(generic.CreateView):
    model = Post
    fields ="__all__"
    success_url= reverse_lazy('blog:all')

class PostUpdteViews(generic.UpdateView):
    model = Post
    fields="__all__"
    sucess_url= reverse_lazy('blog:all')
    
class PostDeleteviews(generic.DeleteView):
    model = Post
    fields = "__all__"
    success_url= reverse_lazy('blog:all')
    
