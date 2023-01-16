from django.urls import path
from .views import SignUpView, LoginView, ProfileView, LogoutView, ProfileUpdateView

app_name = "accounts"
urlpatterns = [
    path("signup", SignUpView.as_view(), name='signup'),
    path("login", LoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name='logout'),
    path("profile/", ProfileView.as_view(), name='profile'),
    path("profile/edit/", ProfileUpdateView.as_view(), name='profile-edit')
]