from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
# Create your views here.
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django import views

class HomeView(views.View):
    def get(self, request):
        products = [{'product':'mobile','price':30},{'product':'laptap','price':3320},{'product':'tablet','price':3000},{'product':'test','price':120}]
        return render(request, 'home.html',context={'products':products})


class LoginViewsli(LoginView):
    template_name =  'test'
    redirect_authenticated_user = True         # اگر کاربر قبلاً وارد شده باشد، او را به صفحه اصلی یا صفحه مشخص‌شده هدایت می‌کند
    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def form_valid(self, form):
        repsonse = super().form_valid(form)
        return redirect('scheduler:apps')
    



class CustomLoginView(FormView):
    template_name = 'registration/login.html'  # قالب فرم لاگین
    form_class = AuthenticationForm            # فرم پیش‌فرض برای ورود
    success_url = reverse_lazy('scheduler:apps')  # مسیر موفقیت پس از لاگین

    def form_valid(self, form):
        # ورود کاربر پس از اعتبارسنجی فرم
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        # بررسی اینکه آیا کاربر قبلاً لاگین کرده است
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().get(request, *args, **kwargs)