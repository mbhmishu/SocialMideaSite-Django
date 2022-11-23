from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from accountapp.models import UserProfile

class CreatNewUser(UserCreationForm):
    email=forms.EmailField(required=True,widget=forms.TextInput(attrs={'placeholder':'@Email' }), label='    ')
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'@Usernames'}), label='   ')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}), label='  ')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password confirmation'}), label='  ')
    
    
    class Meta:
        model = User
        fields = ['email','username',  'password1', 'password2']


class UserProfileEditForm(forms.ModelForm):
    D_O_B = forms.DateField(label='Date of birth',widget=forms.TextInput(attrs={'type':'date',}))
    class Meta:
        model = UserProfile
        exclude = ('user',)

class UserProfileChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email','password')