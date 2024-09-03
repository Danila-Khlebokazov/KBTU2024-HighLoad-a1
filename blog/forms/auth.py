from django.contrib.auth.models import User
from django.forms import Form, fields, widgets


class RegistrationUserForm(Form):
    username = fields.CharField(max_length=100)
    email = fields.EmailField(required=False)
    password = fields.CharField(widget=widgets.PasswordInput)
    confirm_password = fields.CharField(widget=widgets.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise fields.ValidationError('Passwords do not match')
        return cleaned_data

    def save(self):
        data = self.cleaned_data
        user = User.objects.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )
        return user


class LoginUserForm(Form):
    username_or_email = fields.CharField(max_length=100)
    password = fields.CharField(widget=widgets.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username_or_email = cleaned_data.get('username_or_email')
        password = cleaned_data.get('password')
        if '@' in username_or_email:
            users = User.objects.filter(email=username_or_email)
        else:
            users = User.objects.filter(username=username_or_email)
        if not users.exists():
            raise fields.ValidationError('Incorrect password or user does not exist')
        user = users.first()
        if not user.check_password(password):
            raise fields.ValidationError('Incorrect password or user does not exist')
        return cleaned_data
