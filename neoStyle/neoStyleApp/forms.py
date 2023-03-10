from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Newsletter, NewsletterUser

class RegisterForm(UserCreationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(required=True, label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(required=True, label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model=User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    password= forms.CharField(required=True, label="Password", widget=forms.PasswordInput(attrs={'class':'form-control'}))


# Newsletter

class NewsletterUserSignupForm(forms.ModelForm):
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    
    class Meta:
        model = NewsletterUser
        fields = ['email',]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email

