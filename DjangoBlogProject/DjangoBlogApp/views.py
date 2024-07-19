from django.shortcuts import render

# Create your views here.

#Post  Crud Views

from .Django_Blog.create_new_post import CreateNewPost
from .Django_Blog.get_all_posts_list import GetAllPostListApi
from .Django_Blog.get_posts_details_by_id import GetPostsById
from .Django_Blog.update_vendors_details import UpdatePostDetailsById
from .Django_Blog.delete_post_details import DeletePostDetails



CreateNewPost()
GetAllPostListApi()
GetPostsById()
UpdatePostDetailsById()
DeletePostDetails()
