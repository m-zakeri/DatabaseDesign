from django import forms


class CuntactUsForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'ایمیل'}))
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'نام و نام خانوادگی'}))
    message = forms.CharField(max_length=500, widget=forms.Textarea({'placeholder': 'پیام'}))
