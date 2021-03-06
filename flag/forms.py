from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile, NeighbourHood, Business, Post

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class NeighbourHoodForm(forms.ModelForm):
    class Meta:
        model = NeighbourHood
        exclude = ('admin',)     

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user', 'hood')   

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'neighbourhood')

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ('admin',)