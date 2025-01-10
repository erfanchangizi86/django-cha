from django import forms
import django.db
from django.contrib.auth import get_user_model

user = get_user_model()
from django.contrib.auth.hashers import make_password

from django import forms
from django.contrib.auth.models import User  # یا مدل سفارشی شما

class UserForm(forms.ModelForm):
    class Meta:
        model = User  # یا مدل سفارشی شما
        fields = ("username", "email", "password")
        
        # برچسب‌های فارسی
        labels = {
            "username": "نام کاربری",
            "email": "ایمیل",
            "password": "رمز عبور",
        }
        
        # پیام‌های خطای فارسی
        error_messages = {
            "username": {
                "required": "وارد کردن نام کاربری الزامی است.",
                "max_length": "نام کاربری نمی‌تواند بیشتر از 150 کاراکتر باشد.",
                "unique": "این نام کاربری قبلاً ثبت شده است. لطفاً یک نام کاربری دیگر انتخاب کنید.",

            },
            "email": {
                "required": "وارد کردن ایمیل الزامی است.",
                "invalid": "لطفاً یک ایمیل معتبر وارد کنید.",
                "unique": "این نام کاربری قبلاً ثبت شده است. لطفاً یک نام کاربری دیگر انتخاب کنید.",

            },
            "password": {
                "required": "رمز عبور الزامی است.",
            },
        }

    # برای رمز عبور ویجت رمز عبور را تنظیم کنید
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password"].widget = forms.PasswordInput()

    def save(self, commit=True):
        user = super().save(commit=False)
        # هش کردن رمز عبور
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user