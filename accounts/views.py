from django import dispatch
from django.shortcuts import redirect, render
from django.views.generic import UpdateView, FormView, View
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.password_validation import validate_password
from accounts.models import Customer
from accounts.utils.constants import (
    PROFILE_TEMPLATE,
    PROFILE_UPDATE_SUCCESS,
    LOGOUT_SUCCESS,
    LOGIN_TEMPLATE,
    REGISTER_TEMPLATE,
    DASHBOARD_URL,
    LOGIN_SUCCESS,
    LOGIN_ERROR,
    LOGIN_REVERSE,
    PASSWORD_NOT_MATCH,
    SIGNUP_SUCCESS,
    TERMS_NOT_CHECKED,
)
from accounts.forms import CustomerUpdateForm, LoginForm, RegisterForm
from django.urls import reverse_lazy
from django.contrib.messages import info
from django.core.exceptions import ValidationError
from login_required import login_not_required


class ProfileView(UpdateView):
    template_name = PROFILE_TEMPLATE
    model = Customer
    form_class = CustomerUpdateForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        info(self.request, PROFILE_UPDATE_SUCCESS)
        return reverse_lazy("profile", kwargs={"pk": self.request.user.pk})

    def get_queryset(self):
        return Customer.objects.filter(id=self.request.user.pk)


@login_not_required
class LoginView(FormView):
    template_name = LOGIN_TEMPLATE
    form_class = LoginForm
    success_url = DASHBOARD_URL

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"],
        )
        if not user:
            form.add_error(None, LOGIN_ERROR)
            return super().form_invalid(form)
        login(self.request, user)
        info(self.request, LOGIN_SUCCESS)
        return super().form_valid(form)


@login_not_required
class RegisterView(FormView):
    template_name = REGISTER_TEMPLATE
    form_class = RegisterForm
    success_url = reverse_lazy(LOGIN_REVERSE)

    def form_valid(self, form):
        """
        registration form handle, user signed up if form_valid else if password not match user already exist or password valiadtion return form_invalid
        """
        try:
            if self.request.POST.get("termsCondition"):
                password1 = self.request.POST.get("password1")
                password2 = self.request.POST.get("password2")
                validate_password(password1)
                if not password1 == password2:
                    form.add_error(None, PASSWORD_NOT_MATCH)
                    return super().form_invalid(form)
                user = form.save(commit=False)
                user.set_password(password1)
                user.save()
                info(self.request, SIGNUP_SUCCESS)
                return super().form_valid(form)
            else:
                form.add_error(None, TERMS_NOT_CHECKED)
                return super().form_invalid(form)
        except ValidationError as ve:
            form.add_error(None, ve)
            return super().form_invalid(form)


class LogoutView(View):

    def get(self, request):
        logout(request)
        info(request, LOGOUT_SUCCESS)
        return redirect(DASHBOARD_URL)
