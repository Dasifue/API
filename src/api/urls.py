from django.urls import path
from .views.posts import PostListView, PostDetailView, PostCreateView
from .views.coments import ComentListView, ComentDetailView, ComentCreateView



app_name = 'api'

urlpatterns = [
    path('posts/', PostListView.as_view()),
    path('coments/', ComentListView.as_view()),
    path('post_details/<int:post_id>', PostDetailView.as_view()),
    path('coment_details/<int:coment_id>', ComentDetailView.as_view()),
    path('post_create/', PostCreateView.as_view()),
    path('coment_create/', ComentCreateView.as_view()),
]