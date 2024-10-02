from django.http import HttpResponse


def register_view(request):
    return HttpResponse("Register Page")


def login_view(request):
    return HttpResponse("Login Page")


def logout_view(request):
    return HttpResponse("Logout Page")
