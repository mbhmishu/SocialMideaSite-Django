from django.contrib import admin
from accountapp.models import UserProfile,Follow

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Follow)