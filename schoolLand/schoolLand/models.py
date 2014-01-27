from django.db import models
from django.forms import ModelForm

# Create your models here.

class Users(models.Model):
	userName = models.CharField(max_length=100)
	firstName = models.CharField(max_length=100)
	lastName = models.CharField(max_length=100,null=True)
	middleName = models.CharField(max_length=100,null=True)
	email = models.CharField(max_length=150)
	password = models.CharField(max_length=50)
	createdTime = models.DateTimeField('date created')

class UsersForm(ModelForm):
	class Meta:
		model = Users
		#fields = ['firstName', 'lastName', 'email', 'password'] 
		exclude = ['userName', 'middleName', 'createdTime']
