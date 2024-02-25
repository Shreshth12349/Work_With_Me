from django import forms
from .models import Student


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    university_name = forms.CharField(max_length=100)
    university_year = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


# class ProjectForm(forms.Form):
#     title = forms.CharField()
#     description = forms.Textarea()
#     skills = forms.CharField()
#     details = forms.Textarea()

class ProjectForm(forms.Form):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'class': 'my-class'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'my-class'}), label='Description')
    skills = forms.CharField(label='Skills', widget=forms.TextInput(attrs={'class': 'my-class'}))
    details = forms.CharField(widget=forms.Textarea(attrs={'class': 'my-class'}), label='Details')


