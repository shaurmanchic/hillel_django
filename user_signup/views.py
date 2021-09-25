from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import SignUpForm, LogInForm


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            breakpoint()
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'auth.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        breakpoint()
        form = LogInForm(data=request.POST) # https://coderoad.ru/8421200/%D0%98%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-AuthenticationForm-%D0%B2-Django
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = LogInForm()
    return render(request, 'auth.html', {'form': form})
