#from django.db import models
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
# Create your models here.

#class UserProfile(models.Model):
#	hobby = models.CharField(max_length=100)
#	user = models.ForeignKey
	

class UsersForm(ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email', 'password'] 
		#exclude = ['userName', 'middleName', 'createdTime']
	def __init__(self, *args, **kwargs):
		super(UsersForm,self).__init__(*args, **kwargs)
		
		for key in self.fields:
			self.fields[key].required = True
