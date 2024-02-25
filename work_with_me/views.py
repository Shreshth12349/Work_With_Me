from django.shortcuts import render
from .models import Student, Skill, Project, Application
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm, ProjectForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.db import models
import uuid


# Create your views here.

def landing_page(request):
    return render(request, 'landing-page.html')


def home(request):
    # Assuming 'home' is the name of your home URL pattern
    if request.user.is_authenticated:
        # User is authenticated, render the home page
        return render(request, 'home-page.html', {'username': request.user})
    else:
        # User is not authenticated, redirect to the login page
        return redirect('login')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Create a new User object with form data
            new_user = Student(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                university_name=form.cleaned_data['university_name'],
                university_year=form.cleaned_data['university_year'],
                password=form.cleaned_data['password'],
            )
            new_user.save()
            return redirect('landing_page')  # Redirect to a success page
    else:
        form = RegistrationForm()
    return render(request, 'registration-form.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page or homepage
                return redirect('home-page')  # Replace 'home' with the name of your home URL pattern
            else:
                # Authentication failed, display an error message
                return render(request, 'login-page.html', {'form': form, 'error': 'Invalid username or password.'})
    else:
        form = LoginForm()
    return render(request, 'login-page.html', {'form': form})


def post_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            skills = form.cleaned_data['skills']
            details = form.cleaned_data['details']
            creator_id = request.user
            # Create a new Project instance with the provided data
            new_project = Project.objects.create(
                title=title,
                description=description,
                details=details,
                creator_id=creator_id
            )
            # Add skills to the new project (assuming skills is a ManyToManyField)
            new_project.skills_required.set(skills)
            new_project.save()
            # Redirect to a success page or wherever appropriate
            return redirect('home-page')  # Redirect to the home page after successfully creating the project
    else:
        form = ProjectForm()
    return render(request, 'project-create.html', {'form': form})
