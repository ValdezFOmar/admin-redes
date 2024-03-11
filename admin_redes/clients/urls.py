from django.urls import path
from . import views


# TODO:
# Create a tickets/ path and 
# - show all the tickets
# - show a form to issue tickets
urlpatterns = [
    path("", views.home, name='home'),
    path("add-ticket", views.add_ticket, name="add-ticket"),
    path("login-user", views.login_user, name="login-user"),
    path("logout-user", views.logout_user, name="logout-user"),
]
