from django import forms
from .models import Product, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']