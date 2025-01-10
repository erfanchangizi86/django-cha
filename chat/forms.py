from django import forms
import django.db
from django.contrib.auth import get_user_model

user = get_user_model()


class userform(forms.ModelForm):
    class Meta:
        model = user
        fields = ("username", "email", "password")
        