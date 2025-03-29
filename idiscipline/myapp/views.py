from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    return render(request, "myapp/DOlogin.html")  # Ensure this matches your template

def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if user exists with given email
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "Invalid email or password")
            return redirect('login')  # Make sure 'login' is the correct name in urls.py

        # Authenticate using the username (not email)
        user = authenticate(request, username=user.username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Login successfully")
            return redirect('home')  # Redirect to the homepage
        else:
            messages.error(request, "Invalid email or password")

    return render(request, 'myapp/DOlogin.html')  # Use consistent template name
