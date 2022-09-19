from django.contrib.auth.models import User
from django.forms import ModelForm, forms
from django import forms
from users.models import CustomUserModel, StoofersCard
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")


class CustomUserform(ModelForm):
    phone = forms.CharField(error_messages={"unique": "Phone No. already registered."})

    class Meta:
        model = CustomUserModel
        fields = ("phone", "college", "pincode")


class Cardform(ModelForm):
    class Meta:
        model = StoofersCard
        fields = ("name",)
