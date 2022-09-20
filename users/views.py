from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from users.forms import SignupForm, CustomUserform, Cardform
from users.models import StoofersCard, CustomUserModel
from django.contrib.auth import get_user_model

current_user = get_user_model()


@csrf_exempt
def login(request):
    return render(request, "registration/login.html")


def logout_user(request):
    auth.logout(request)
    return redirect("login")


@csrf_exempt
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            raw_password = form.cleaned_data.get("password1")

            user = authenticate(username=user.username, password=raw_password)
            login(request)
            return redirect("login")
    else:
        form = SignupForm()
    return render(request, "signup.html", {"form": form})


@login_required
def stooferscard(request):
    context = {}
    form = Cardform(request.POST or None, request.FILES or None)

    if form.is_valid():
        url = form.save(commit=False)
        url.user = request.user
        url.save()
        return render(request, "card.html", {"new": url, "form": form})

    return render(request, "card.html", {"new": None, "form": form})


@login_required
def customer(request):
    context = {}
    form = CustomUserform(request.POST or None, request.FILES or None)

    if form.is_valid():
        url = form.save(commit=False)
        url.user = request.user
        url.save()
        return redirect("stooferscard")
    context["form"] = form
    return render(request, "customuser.html", context)


def error_404_view(request, exception):
    return redirect("https://stoofers.com")
