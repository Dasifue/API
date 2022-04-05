from django.shortcuts import render, redirect
from ..models import Coment
from ..forms import ComentCreateForm


def post_coments(request, post_id):
    coments = Coment.objects.filter(post = post_id)
    return coments


def create_coment(request, post_id):
    form = ComentCreateForm()
    if request.method == "POST":
        save_form = ComentCreateForm(request.POST)
        if save_form.is_valid():
            save_form.save()
    return render(request, 'create_coment.html', {'form':form})


def delete_coment(request, coment_id):
    coment = Coment.objects.filter(id = coment_id).delete()
    return redirect('project:all_posts')

