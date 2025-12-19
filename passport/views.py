from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PassportForm

@login_required
def add_passport(request):
    if hasattr(request.user, 'passport'):
        return render(request, 'passport/already_exists.html')

    if request.method == 'POST':
        form = PassportForm(request.POST)
        if form.is_valid():
            passport = form.save(commit=False)
            passport.user = request.user
            passport.save()
            return redirect('passport_success')
    else:
        form = PassportForm()

    return render(request, 'passport/add_passport.html', {'form': form})
