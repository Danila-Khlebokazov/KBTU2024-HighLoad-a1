from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import View

from blog.forms.auth import RegistrationUserForm


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
