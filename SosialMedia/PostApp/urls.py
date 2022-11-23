from django.urls import path
from PostApp import views

app_name = 'postapp'


urlpatterns = [
    path('home/', views.home, name='home'),
    path('user_like/<pk>/', views.user_like, name='user_like'),
    path('user_unlike/<pk>/', views.user_unlike, name='user_unlike'),
    path('UdatePost/<pk>/', views.UdatePost.as_view(), name='UdatePost'),

    
]
