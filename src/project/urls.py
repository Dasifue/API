from django.urls import path
from .views.posts import all_posts, post_info, reset_upvotes, create_post, delete_post
from .views.coments import create_coment, delete_coment


app_name = 'project'

urlpatterns = [    
    path('all_posts/', all_posts, name='all_posts'),
    path('post_info/<int:post_id>', post_info, name='post_info'),
    path('reset_upvotes/', reset_upvotes, name='reset_upvotes'),
    path('create_post/', create_post, name='create_post'),
    path('create_coment/<int:post_id>', create_coment, name='create_coment'),
    path('delete_post/<int:post_id>', delete_post, name='delete_post'),
    path('delete_coment/<int:coment_id>', delete_coment, name='delete_coment')
]