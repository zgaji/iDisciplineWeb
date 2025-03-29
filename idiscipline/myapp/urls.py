from django.urls import path
from .views import login_view, home  # Import your home view if needed

urlpatterns = [
    path("", home, name="home"),  # Home page
     path('login/', login_view, name='login'),
]

