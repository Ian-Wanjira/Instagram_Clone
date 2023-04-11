from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginForm

class CustomLogoutView(LogoutView):
    template_name = 'accounts/logout.html'
    