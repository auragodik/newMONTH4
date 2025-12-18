from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from users.models import CustomUser
from users.forms import CustomUserForm, LoginForm

def user_list_view(request):
    users_list = CustomUser.objects.all().order_by('-id')
    return render(request, 'users/user_list.html', {'users_list': users_list})

def auth_logout_view(request):
    logout(request)
    return redirect('login')

def auth_login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('users_list')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserForm()
    return render(request, 'users/create_user.html', {'form': form})
