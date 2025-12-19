from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PassportForm
from .models import Passport

class AddPassportView(LoginRequiredMixin, View):
    def get(self, request):
        if Passport.objects.filter(user=request.user).exists():
            return render(request, 'passport/already_exists.html')
        form = PassportForm()
        return render(request, 'passport/add_passport.html', {'form': form})

    def post(self, request):
        if Passport.objects.filter(user=request.user).exists():
            return render(request, 'passport/already_exists.html')
        form = PassportForm(request.POST)
        if form.is_valid():
            passport = form.save(commit=False)
            passport.user = request.user
            passport.save()
            return redirect('passport_success')
        return render(request, 'passport/add_passport.html', {'form': form})
