from django import forms
from django.contrib.auth.hashers import make_password

from home.models import AnalystUser


class RegisterForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=64, widget=forms.PasswordInput())
    confirmed_password = forms.CharField(max_length=64, widget=forms.PasswordInput())

    def clean_email(self):
        email = self.cleaned_data['email']

        try:
            _ = AnalystUser.objects.get(email=email)
            raise forms.ValidationError(f'User with email {email} already exists.')
        except AnalystUser.DoesNotExist:
            return email

    def clean(self):
        password = self.cleaned_data['password']
        confirmed_password = self.cleaned_data['confirmed_password']

        if password != confirmed_password:
            self.add_error('password', 'Passwords must be equal')

    def save(self):
        user = AnalystUser.objects.create(
            email=self.cleaned_data['email'],
            password=make_password(self.cleaned_data['password']),
        )
        return user

    def get_email(self):
        return self.cleaned_data['email']
