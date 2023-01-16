from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserCreateForm, UserUpdateForm


# Create your views here.
class SignUpView(View):
    def get(self, request):
        create_form = UserCreateForm()
        context = {
            "form": create_form
        }
        return render(request, "accounts/signup.html", context)

    def post(self, request):
        create_form = UserCreateForm(data=request.POST)

        if create_form.is_valid():
            # forms.py ichida save() funksiyasi bor
            create_form.save()

            # create user account
            return redirect('accounts:login')
        else:
            context = {
                "form": create_form
            }

            return render(request, "accounts/signup.html", context)


class LoginView(View):
    def get(self, request):
        login_form = AuthenticationForm()

        return render(request, "accounts/login.html", {"login_form": login_form})

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)

        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)

            messages.success(request, "You have successfully logged in.")

            return redirect('home_page')
        else:
            return render(request, "accounts/login.html", {"login_form": login_form})
            

class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.info(request, "You have successfully logged out.")
        return redirect("home_page")


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):

        # WE CAN DELETE THE FOLLOWING LINES OF CODE BECAUSE LoginRequiredMixin itself does it instead.
        # IF A USER IS NOT LOGGED IN AND WANTS TO OPEN PROFILE PAGE, IT REDIRECTS TO LOGIN PAGE
        # if not request.user.is_authenticated:
        #     return redirect("users:login")

        return render(request, "accounts/profile.html", {'users': request.user})



class ProfileUpdateView(LoginRequiredMixin, View):
    def get(self, request):
        user_update_form = UserUpdateForm(instance=request.user)
        return render(request, "accounts/profile_edit.html", {"form": user_update_form})

    def post(self, request):
        user_update_form = UserUpdateForm(
            instance=request.user,
            data=request.POST,
            files=request.FILES
        )

        if user_update_form.is_valid():
            user_update_form.save()
            messages.success(request, "You have successfully updated your profile.")

            return redirect("accounts:profile")

        return render(request, "accounts/profile_edit.html", {"form": user_update_form})