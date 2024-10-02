from django.http import HttpResponse
from django.shortcuts import render

from users.form import RegisterForm


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user['is_active'] = False
            user.save()
            return render(request, "auth/login.html")

    return render(request, "auth/register.html")


def login_view(request):
    return render(request, "auth/login.html")


def logout_view(request):
    return HttpResponse("Logout Page")
