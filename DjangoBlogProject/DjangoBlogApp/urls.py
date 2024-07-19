from django.urls import path,include
from .views import CreateNewPost,GetAllPostListApi,GetPostsById,UpdatePostDetailsById,DeletePostDetails

# Vendor CRUD URLs
urlpatterns = [
    path('CreateNewPost/', CreateNewPost.as_view()),
    path('GetAllPostListApi/', GetAllPostListApi.as_view()),
    path('GetPostsById/<int:id>/', GetPostsById.as_view()),
    path('UpdatePostDetailsById/<int:id>/', UpdatePostDetailsById.as_view()),
    path('DeletePostDetails/<int:id>/', DeletePostDetails.as_view()),
]


