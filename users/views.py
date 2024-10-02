from django.http import HttpResponse
from django.shortcuts import render


def register_view(request):
    if request.method == "POST":
        pass
    return render(request, "auth/register.html")


def login_view(request):
    return render(request, "auth/login.html")


def logout_view(request):
    return HttpResponse("Logout Page")
