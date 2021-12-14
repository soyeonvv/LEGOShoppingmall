from django.shortcuts import render

from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.

class PostList(ListView):
    model = Post
    ordering = '-pk'
    paginate_by = 6

    template_name = 'shopping/lego_list.html'

class PostDetail(DetailView):
    model = Post
    

