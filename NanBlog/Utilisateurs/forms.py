from django import forms
from .models import *
from django.contrib.auth.models import Group


# class RegistrationForm(forms.ModelForm):
#     class Meta:
#         model = MyUser
#         fields =(
# 			'groups',
#             'first_name',
#             'last_name',
#             'description',
# 		)
#     def signup(self, request, user):
#         # Save your user
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#         user.description = self.cleaned_data['description']
#         group = self.cleaned_data['groups']
#         g = Group.objects.get(name=group[0])
#         user.groups.add(g)
#         user.save()

from allauth.account.forms import SignupForm
class RegistrationForm(SignupForm, forms.ModelForm):

    class Meta:
        model = MyUser
        fields =(
			'groups',
            'first_name',
            'last_name',
            'description',
		)
        labels = {'groups': 'Type de compte', 'description': 'Votre Bio'}
    def save(self, request):
        # group = self.cleaned_data['groups']
        # g = Group.objects.get(name=group[0])
        # print(g)
        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(RegistrationForm, self).save(request)

        # Add your own processing here.

        # You must return the original result.
        return user
# class EtablissementRegistrationForm(UserCreationForm):
# 	class Meta:
# 		model=EtablissementUser
# 		fields =(
# 			'username',
# 			'email',
#             'first_name',
#             'last_name',
#             'contact',
#             'avatar',
# 			'password1',
# 			'password2',
# 		)

# class EditProfileForm(UserChangeForm):

# 	class Meta:
# 		model = User
# 		fields = (
#             'username',
# 			'email',
# 			'first_name',
# 			'last_name',
# 			'contact',
#             'bio', 
# 			)
