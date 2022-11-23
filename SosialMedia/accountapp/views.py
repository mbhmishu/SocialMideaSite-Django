from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from accountapp.forms import CreatNewUser, UserProfileEditForm,UserProfileChangeForm
from accountapp.models import UserProfile, Follow
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from PostApp.forms import PostForm
from PostApp.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.

def user_signup(request):
    form = CreatNewUser()
    registerd = False
    if request.method == 'POST':
        form = CreatNewUser(data=request.POST)
        if form.is_valid():
            user = form.save()
            registerd = True
            user_profile = UserProfile(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse('accountapp:login'))
    return render(request, 'Account/sing_up.html', {'form': form, 'registerd': registerd})

def user_login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('postapp:home'))
            return HttpResponseRedirect('hii')
    return render(request, 'Account/login.html', {'form': form, 'title': 'Login'})


@login_required
def edit_prfile(request):
    current_user = UserProfile.objects.get(user=request.user)
    form = UserProfileEditForm(instance=current_user)
    if request.method == "POST":
        form = UserProfileEditForm(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save(commit=True)
            form = UserProfileEditForm(instance=current_user) 
            return HttpResponseRedirect(reverse('accountapp:profile'))      
    return render(request, 'Account/edit_profile.html', context={'form':form})



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('accountapp:login'))



@login_required
def user_profile(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('postapp:home'))
    
    return render(request, 'Account/user_profile.html', context={'form': form,})





@login_required
def view_profile(request, username):
    result_user = User.objects.get(username=username)
    alrady_follow = Follow.objects.filter(follower=request.user,following=result_user)
    if result_user == request.user:
        return HttpResponseRedirect(reverse('accountapp:profile'))
        
    return render(request, 'Account/view_profile.html', context={'result_user': result_user, 'alrady_follow':alrady_follow})

@login_required
def follow(request, username):
    to_follow = User.objects.get(username=username)
    from_follow = request.user
    alrady_follow = Follow.objects.filter(follower=from_follow,following=to_follow)
    if not alrady_follow:
        followed = Follow(follower=from_follow,following=to_follow)
        followed.save()
        return HttpResponseRedirect(reverse('accountapp:view_profile', kwargs={'username':username}))

        
@login_required
def unfollow(request, username):
    to_follow = User.objects.get(username=username)
    from_follow = request.user
    alrady_follow = Follow.objects.filter(follower=from_follow,following=to_follow)
    alrady_follow.delete()
    return HttpResponseRedirect(reverse('accountapp:view_profile', kwargs={'username':username}))



@login_required
def ChangePasss(request):
    current_user = request.user
    Change_passowrd = PasswordChangeForm(current_user)
    if request.method == 'POST':
        form = PasswordChangeForm(current_user, request.POST,)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('accountapp:view_profile'))
    return render(request,'Account/change_pass.html', context={'Change_passowrd':Change_passowrd})


@login_required
def ChangeUser(request):
    current_user = request.user
    form = UserProfileChangeForm(instance=current_user)
    if request.method == 'POST':
        form = UserProfileChangeForm(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('accountapp:profile'))
    return render(request,'Account/change_user.html', context={'form':form})



