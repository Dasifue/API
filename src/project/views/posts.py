from django.shortcuts import render, redirect
from .coments import post_coments, create_coment
from ..models import Post
from ..forms import PostCreateForm


def all_posts(request):
    posts = Post.objects.all()
    return render(request, 'all_posts.html', {'posts':posts})

def post_info(request, post_id):
    post = Post.objects.get(id = post_id) 
    make_upvote(request, post_id=post_id) 
    return render(request, 'post_info.html', {'post':post, 'coments':post_coments(request, post_id)})


def make_upvote(request, post_id):
    post = Post.objects.get(id = post_id)
    if request.method == 'POST':    
        post.upvotes += 1
        post.save()
    

def reset_upvotes(request):
    posts = Post.objects.all()
    posts.update(upvotes = 0)
    return redirect('project:all_posts')

def create_post(request):
    form = PostCreateForm
    if request.method == 'POST':
        save_form = PostCreateForm(request.POST)
        if save_form.is_valid():
            save_form.save()
        return redirect('project:all_posts')
    return render(request, 'create_post.html', {'form':form})
    


def delete_post(request, post_id):
    deleted_post = Post.objects.filter(id = post_id).delete()
    return redirect('project:all_posts')


    


