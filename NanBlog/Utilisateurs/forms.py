from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.account.forms import *

class RegistrationForm(SignupForm):
    
    class Meta:
        model=MyUser
        fields =(
			'username',
			'email',
            'first_name',
            'last_name',
            'groups',
            'description',
            'image',
			'password1',
			'password2',
		)


class EditProfileForm(UserChangeForm):

	class Meta:
		model = MyUser
		fields = (
            'username',
			'email',
            'first_name',
            'last_name',
            'groups',
            'description',
			)