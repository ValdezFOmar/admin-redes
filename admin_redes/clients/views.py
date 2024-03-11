from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import TicketForm


def home(request: HttpRequest):
    return render(request, "clients/home.html")


def login_user(request: HttpRequest):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials, try again")
            return redirect("login-user")

    return render(request, "clients/login.html")


def logout_user(request: HttpRequest):
    logout(request)
    messages.info(request, "Logout successful")
    return redirect("login-user")


@login_required(login_url="login-user")
def add_ticket(request: HttpRequest):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.reported_date = timezone.now()
            ticket.user = request.user
            ticket.save()
            messages.success(request, "Your ticket has been registered")
            return redirect("add-ticket")
    else:
        form = TicketForm

    context = {"form": form}
    return render(request, "clients/add-ticket.html", context)
