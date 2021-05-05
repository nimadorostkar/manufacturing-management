from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Profile, Ticket, Process
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
	to = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.Select(), error_messages={'required': 'این فیلد ضروری است'} )

	class Meta:
		model = Ticket
		fields = ['to','title','descriptions']






#------------------------------------------------------------------------------
class MaterialForm(forms.ModelForm):
	manager = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.Select(), error_messages={'required': 'این فیلد ضروری است'} )
	#CHOICES = ( ('M','Material'), ('R','Repository'), ('T','Transfer'), ('S','Station'),('P','Product') )
	#position = forms.Select(choices=CHOICES,attrs={'class': 'form-control'}),


	class Meta:
		model = Process
		fields = ['name', 'description','inventory','min_inventory','manager','supplier']







# Form End
