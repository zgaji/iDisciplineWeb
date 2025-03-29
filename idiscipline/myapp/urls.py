from django.urls import path
from .views import user_login, user_logout, home  # Import your home view if needed

urlpatterns = [
    path("", home, name="home"),  # Home page
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
]

