from django.urls import path
from . import views

app_name = 'accountapp'

urlpatterns = [
    path('', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('edit_prfile/', views.edit_prfile, name='edit_prfile'),
    path('user_logout/', views.user_logout, name='logout'),
    path('user_profile/', views.user_profile, name='profile'),
    path('view_profile/<username>/', views.view_profile, name='view_profile'),
    path('follow/<username>/',views.follow, name='follow'),
    path('unfollow/<username>/',views.unfollow, name='unfollow'),
    path('ChangePasss/', views.ChangePasss, name='change_passs'),
    path('ChangeUser/', views.ChangeUser, name='ChangeUser')


    
    
]
