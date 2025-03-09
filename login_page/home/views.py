from django.shortcuts import render,redirect
from django.contrib import messages
from django.views.decorators.cache import never_cache

# Create your views here.

VALID_USERNAME = "shibil"
VALID_PASSWORD = "shibil123"

@never_cache
def login_view(request):
    if 'user' in request.session:
        return redirect('home')  

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == VALID_USERNAME and password == VALID_PASSWORD:
            request.session['user'] = username
            return redirect('home')
        else:
            messages.error(request, "Incorrect username or password")

    return render(request, "login.html")

def logout_view(request):
    request.session.flush()  
    return redirect('login')

@never_cache
def home_view(request):
    if 'user' not in request.session:
        return redirect('login') # Prevent access without login
    return render(request, "home.html")