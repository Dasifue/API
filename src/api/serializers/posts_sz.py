from email.policy import default
from project.models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(
        read_only=True
    )
    upvotes = serializers.IntegerField(
        allow_null=True,
        read_only=True
    )

    class Meta:
        model = Post
        fields = '__all__'


class PostCreateSerializer(serializers.ModelSerializer):
    upvotes = serializers.IntegerField(
        default=0,
        allow_null=True,
        read_only=True
    )
    class Meta:
        model = Post
        fields = '__all__'
