from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import PostForm
from .models import PostModel
from account.models import Profile


class HomeView(View):
    def get(self,request, *args, **kwargs):
        profile = Profile.objects.all()
        form = PostForm()

        posts = PostModel.objects.all().order_by("-posted_date")
        context = {
            "profile": profile,
            "form": form,
            "posts": posts
        }
        return render(request, 'home.html', context)

    def post(self,request,*args, **kwargs):
        print("create_post fn")
        if request.method == 'POST':
            post = request.POST['post']
            print(post)
            new_post = PostModel(post=post, author=request.user)
            new_post.save()
            return HttpResponse("New post created")


def delete_post(request,*args,**kwargs):
    id = kwargs.get("post_id")
    post = PostModel.objects.get(id=id)
    post.delete()
    return redirect("home")


def like(request, *args, **kwargs):
    post_id = kwargs.get("post_id")
    post = PostModel.objects.get(id=post_id)
    post.liked_by.add(request.user)
    post.save()

    return redirect("home")


def unlike(request, *args, **kwargs):
    post_id = kwargs.get("post_id")
    post = PostModel.objects.get(id=post_id)
    post.liked_by.remove(request.user)
    post.save()
    return redirect("home")
