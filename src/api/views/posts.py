from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from api.serializers.posts_sz import PostSerializer, PostCreateSerializer
from project.models import Post


class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'post_id'


class PostCreateView(CreateAPIView):
    serializer_class = PostCreateSerializer