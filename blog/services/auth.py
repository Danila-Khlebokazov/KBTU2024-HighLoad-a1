from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View

from blog.forms.auth import LoginUserForm
from blog.forms.auth import RegistrationUserForm


def registration(request):
    if request.method == 'POST':
        form = RegistrationUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationUserForm()
    return render(request, 'blog/registration.html', {'form': form})


class LoginUserView(View):
    def get(self, request):
        form = LoginUserForm()
        return render(request, 'blog/login.html', {'form': form})

    def post(self, request):
        form = LoginUserForm(request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data['username_or_email']
            password = form.cleaned_data['password']

            # Authenticate user
            user = None
            if '@' in username_or_email:
                user = authenticate(request, email=username_or_email, password=password)
            else:
                user = authenticate(request, username=username_or_email, password=password)

            if user is not None:
                login(request, user)
                return redirect('post_list')  # Redirect to a home page or dashboard after login
            else:
                form.add_error(None, 'Invalid credentials')

        return render(request, 'blog/login.html', {'form': form})


class RegisterUserView(View):
    def get(self, request):
        form = RegistrationUserForm()
        return render(request, 'blog/registration.html', {'form': form})

    def post(self, request):
        form = RegistrationUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('post_list')  # Redirect to a home page or dashboard after registration
        return render(request, 'blog/registration.html', {'form': form})
