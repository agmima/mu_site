from django.urls import path
from .views import CreatePost, ListPost, PostDetailView, EditPost, DeletePost

urlpatterns = [
    path('', ListPost.as_view(),name='home'),
    path('create/', CreatePost.as_view(), name='Create'),
    path('post/detail/<pk>', PostDetailView.as_view(), name='post_detail'),
    path('post/edit/<pk>', EditPost.as_view(), name='post_edit'),
    path('post/delete/<pk>', DeletePost.as_view(), name='post_delete'),





]
