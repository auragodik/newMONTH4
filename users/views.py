from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser
from .forms import CustomUserForm, LoginForm

class UserListView(LoginRequiredMixin, View):
    def get(self, request):
        users_list = CustomUser.objects.all().order_by('-id')
        return render(request, 'users/user_list.html', {'users_list': users_list})

class AuthLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

class AuthLoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('users_list')
        return render(request, 'users/login.html', {'form': form})

class RegisterView(View):
    def get(self, request):
        form = CustomUserForm()
        return render(request, 'users/create_user.html', {'form': form})

    def post(self, request):
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'users/create_user.html', {'form': form})
