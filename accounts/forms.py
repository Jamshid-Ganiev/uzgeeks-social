from django import forms

from .models import CustomUser


class UserCreateForm(forms.ModelForm):
    email = forms.CharField(max_length=75, required=True)
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        widgets = {'password': forms.PasswordInput()}
        help_texts = {
            'username': None,
        }

    def save(self, commit=True):
        # parent class ni save metodi chaqiriladi
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.save()

        return user


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=128)

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'profile_picture')
        help_texts = {
            'username': None,
        }