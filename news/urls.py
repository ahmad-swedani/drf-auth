from django.contrib import admin
from django.urls import path, include

# from .models import Post
from .views import allPosts, postDetail

urlpatterns = [
    path('', allPosts.as_view(), name='all_posts'),
    path('<int:pk>', postDetail.as_view(), name='post_details')
]
