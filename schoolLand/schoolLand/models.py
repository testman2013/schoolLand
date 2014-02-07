from django.db import models
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
# Create your models here.

#class UserProfile(models.Model):
#	hobby = models.CharField(max_length=100)
#	user = models.ForeignKey
	


class images(models.Model):
        image = models.ImageField(upload_to='images')
        sectionId = models.IntegerField(null=True, blank=True)
        active    = models.BooleanField(default=True)
        createdTime = models.DateTimeField(auto_now_add=True, blank=True, null=True)
        #imageName = models.CharField(max_length=100)
        #caption   = models.CharField(max_length=400,null=True)
        #active    = models.BooleanField(default=True)
        #createdTime = models.DateTimeField(auto_now_add=True, blank=True, null=True)
        
class pdf(models.Model):
        uploadedFile      = models.FileField(upload_to='files')
        active            = models.BooleanField(default=True)
        sectionId = models.IntegerField(null=True, blank=True)
        createdTime       = models.DateTimeField(auto_now_add=True, blank=True, null=True)

class messages(models.Model):
        message = models.TextField(null=True, blank=True)
        user    = models.ForeignKey(User)
        createdTime = models.DateTimeField(auto_now_add=True, blank=True, null=True)
