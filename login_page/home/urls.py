from django.urls import path
from .views import login_view, home_view, logout_view

urlpatterns = [
    path("", login_view, name="login"),  # Login page
    path("home/", home_view, name="home"),  # Homepage (after login)
    path("logout/", logout_view, name="logout"),  # Logout route
]