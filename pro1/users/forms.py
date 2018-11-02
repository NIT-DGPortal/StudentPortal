# extra email field after inherited form.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()  #default is true that is is required
	# add validation for institute email id

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']  # in-order
