from django.shortcuts import render, redirect
from .models import AuthToken, User
from django.contrib.auth import authenticate
from .utils import generate_otp


def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        if email and password:
            user = authenticate(email=email, password=password)
            print(user)
            if user:
                token_obj, created = AuthToken.objects.get_or_create(user=user)
                if created:
                    token_obj.token = AuthToken.generate_token()
                    token_obj.save()
                return render(
                    request, "dashboard.html", {"user": user}, status=200
                ).set_cookie("token", token_obj.token, httponly=True, secure=True)
            return render(
                request,
                "login.html",
                {"error": "Invalid email or password"},
                status=404,
            )
    return render(request, "login.html")


def signup(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        if first_name and last_name and username and email and password :
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password,
            )
            print("User",user)
            code = generate_otp()
            if code:
                user.verificationCode = code
                user.email_user('Verification Code',code,'hamnatariq663@gmail.com')
                user.save()
                return redirect("login")
    return render(request, "signup.html")
