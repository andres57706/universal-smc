from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy

from ..forms.registration_form import RegistrationForm
from ..forms.signin_form import SigninForm


def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=True)

            # login user
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.email, password=raw_password)
            login(request, user)

            # redirect to home
            return redirect(reverse_lazy('searches:index'))  # TODO: redirect to my recent searches
    else:
        form = RegistrationForm()
    return render(request, "signup/show.html", {'form': form})


class SigninViewClass(LoginView):
    redirect_authenticated_user = True
    form_class = SigninForm
    template_name = "signin/show.html"
    next_page = reverse_lazy('searches:index')


class SignoutViewClass(LogoutView):
    next_page = reverse_lazy('users:signin')
