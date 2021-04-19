from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth.models import User
from .models import Profile, Ticket
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm





#------------------------------------------------------------------------------
class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['phone','address','user_photo']



#------------------------------------------------------------------------------
class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','first_name','last_name','email','password1','password2']


#------------------------------------------------------------------------------
class TicketForm(forms.ModelForm):
	to = forms.CharField(error_messages={'required': 'ضروری'})

	class Meta:
		model = Ticket
		fields = ['to','title','descriptions']
