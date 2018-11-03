# extra email field after inherited form.py
# Registration form

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField(required = True)  
	
	#default is true that it is required
	# add validation for institute email id

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']  # in-order

	def clean_email (self) :
		data = self.cleaned_data['email']
		domain = data.split('@')[1]
		if domain != 'btech.nitdgp.ac.in' :
			raise forms.ValidationError('Please make sure that you use college mail address')
		return data