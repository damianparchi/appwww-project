from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, SetPasswordForm, PasswordResetForm
from django.contrib.auth.models import User
from .models import Client

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus' : 'True', 'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus':'True', 'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Stare hasło', widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class': 'form-control'}))
    new_password1 = forms.CharField(label='Nowe hasło', widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class': 'form-control'}))
    new_password2 = forms.CharField(label='Potwierdź hasło', widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class': 'form-control'}))

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label="Nowe hasło", widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
    new_password2 = forms.CharField(label="Potwierdź nowe hasło", widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))

class ClientProfileForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['imie', 'miasto', 'ulica','numer_domu_mieszkania', 'telefon', 'wojewodztwo','kodPocztowy']
        widgets = {
            'imie':forms.TextInput(attrs={'class':'form-control'}),
            'miasto':forms.TextInput(attrs={'class':'form-control'}),
            'ulica':forms.TextInput(attrs={'class':'form-control'}),
            'numer_domu_mieszkania':forms.NumberInput(attrs={'class':'form-control'}),
            'telefon':forms.NumberInput(attrs={'class':'form-control'}),
            'wojewodztwo':forms.Select(attrs={'class':'form-control'}),
            'kodPocztowy':forms.NumberInput(attrs={'class':'form-control'}),
        }