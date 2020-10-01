from django.shortcuts import render
from rest_framework import generics

# Create your views here.
from .models import Post
from .serializer import PostSerializer

class allPosts(generics.ListCreateAPIView):
     queryset = Post.objects.all()
     serializer_class = PostSerializer
     

class postDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer