from django.db import models


class Post(models.Model):

    title = models.CharField(
        verbose_name='Post name',
        max_length=50,  
        blank=False,
        null=False)
    link = models.URLField(
        verbose_name='Post link',
        max_length=200,
        null=False,
        blank=False
    )
    creation_date = models.DateTimeField(
        verbose_name='Create date',
        auto_now_add=True,
        editable=False)
    upvotes = models.IntegerField(
        default=0
        )
    author = models.CharField(
        verbose_name='Author name',
        max_length=50,
        blank=False,
        null=False
    )
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class Coment(models.Model):

    author = models.CharField(
        verbose_name='Author name',
        max_length=50,
        blank=False,
        null=False
    )
    content = models.TextField(
        verbose_name='Comment content',
        max_length=1000,
        blank=False,
        null=False
    )
    creation_date = models.DateTimeField(
        verbose_name='Creation date',
        auto_now_add=True,
        editable=False
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='Post',
        blank=True
    )

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'Coment'
        verbose_name_plural = 'Coments'
