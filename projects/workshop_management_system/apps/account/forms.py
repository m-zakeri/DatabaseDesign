from django import forms
from django.contrib.auth import authenticate

from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.password_validation import validate_password
from .models import *


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["username", "email"]

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = '__all__'


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'username or email'}))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'placeholder': 'password'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if '@' in username and username[-10:] != '@gmail.com':
            raise ValidationError('Please enter the correct email')
        if '@' not in username and len(username) > 50:
            raise ValidationError('The maximum length of the username is 50 characters')
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError('Your password must be at least 8 characters long')
        return password

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if not authenticate(username=username, password=password):
            raise ValidationError('The username or password is incorrect')


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'username'}))
    email = forms.EmailField(widget=forms.EmailInput({'placeholder': 'email'}))
    password = forms.CharField(max_length=20, validators=[validate_password],
                               widget=forms.PasswordInput({'placeholder': 'password'}))
    confirm_password = forms.CharField(max_length=20, validators=[validate_password],
                                       widget=forms.PasswordInput({'placeholder': 'confirm password'}))

    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError('Your password and confirmation password do not match.')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) > 50:
            raise ValidationError('The maximum length of the username is 50 characters')
        return username


class VerifyEmailForm(forms.Form):
    randcode = forms.CharField(max_length=5, widget=forms.TextInput(attrs={'placeholder': 'Please enter the code'}))


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'email'}))


class ChangePasswordForm(forms.Form):
    password = forms.CharField(max_length=20, validators=[validate_password],
                               widget=forms.PasswordInput({'placeholder': 'password'}))
    confirm_password = forms.CharField(max_length=20, validators=[validate_password],
                                       widget=forms.PasswordInput({'placeholder': 'confirm password'}))

    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            return VerifyEmailForm('Your password and confirmation password do not match.')
