from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import todo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password 
from django.conf import settings
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


# Create your views here.

@permission_classes((IsAuthenticated,))
def home(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        # Check if a task with the same name already exists
        if todo.objects.filter(user=request.user, todo_name=task).exists():
            messages.error(request, 'Task with this name already exists.')
            return redirect('register')
        else:
            new_todo = todo(user=request.user, todo_name=task)
            new_todo.save()

    all_todos = todo.objects.filter(user=request.user) 
    context = {
        'todos': all_todos
    }
    return render(request, "todoapp/todo.html", context)

def register(request):
    if request.user.is_authenticated:
        return redirect('home-page')
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        print(username,password,email)

        if len(password) < 7:
            messages.error(request, 'Password must be at least 8 characters')
            return redirect('register')

        get_all_users_by_username = User.objects.filter(username=username)
        if get_all_users_by_username:
            messages.error(request, 'Error, username already exists, User another.')
            return redirect('register')

        new_user = User.objects.create_user(username=username, email=email, password=password)
        new_user.save()

        messages.success(request, 'User successfully created, login now')
        return redirect('login')
    return render(request, 'todoapp/register.html', {})


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home-page')
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')

        validate_user = authenticate(username=username, password=password)
        if validate_user is not None:
            login(request, validate_user)
            return redirect('home-page')
        else:
            messages.error(request, 'Error, wrong user details or user does not exist')
            return redirect('login')


    return render(request, 'todoapp/login.html', {})

# @login_required
@permission_classes([IsAuthenticated])
def DeleteTask(request, name):
    get_todo = todo.objects.get(user=request.user, todo_name=name)
    get_todo.delete()
    return redirect('home-page')

# @login_required
# Mark as Complete
@permission_classes([IsAuthenticated])
def Update(request, name):
    get_todo = todo.objects.get(user=request.user, todo_name=name)
    get_todo.status = True
    get_todo.save()
    return redirect('home-page')


def LogoutView(request):
    logout(request)
    return redirect('login')

