from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accountapp.models import UserProfile, Follow
from PostApp.models import Post,Like
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

@login_required
def home(request):
    following_list = Follow.objects.filter(follower=request.user)
    posts = Post.objects.filter(author__in=following_list.values_list('following'))
    post_like= Like.objects.filter(user=request.user)
    post_like_list = post_like.values_list('post', flat=True)
    
    if request.method == "GET":
        Search = request.GET.get('Search', '')
        results = User.objects.filter(username__icontains=Search)

    return render(request, 'Account/home.html', context={'results': results, 'Search': Search,'posts': posts, 'post_like_list':post_like_list})



@login_required
def user_like(request, pk):
    post = Post.objects.get(pk=pk)
    alrady_like = Like.objects.filter(post=post, user=request.user)
    if not alrady_like:
        post_like = Like(post=post, user=request.user)
        post_like.save()
        return HttpResponseRedirect(reverse('postapp:home'))
    

@login_required
def user_unlike(request, pk):
    post = Post.objects.get(pk=pk)
    alrady_like = Like.objects.filter(post=post, user=request.user)
    alrady_like.delete()
    return HttpResponseRedirect(reverse('postapp:home'))



class UdatePost(LoginRequiredMixin, UpdateView):
    context_object_name = 'form'
    model= Post
    fields=('caption','img')
    template_name= 'postapp/edit_post.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('accountapp:profile')


    