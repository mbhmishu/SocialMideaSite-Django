from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='users')
    D_O_B= models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    P_P = models.ImageField(upload_to='userImg/profilepic', blank=True, null=True  )
    

    def __str__(self):
        return self.user.username

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE ,related_name='followers')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    date = models.DateTimeField(auto_now_add=True)
