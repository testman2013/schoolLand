from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from schoolLand.models import Users
from schoolLand.models import UsersForm
#from schoolLand import models
import datetime
from django import forms 
from django.forms.models import modelformset_factory
# Create your views here.



def index(request):
	return render(request, 'schoolLand/index.html')

def signUp(request):
	#UsersFormSet = modelformset_factory(Users)
	#if(request.POST):
        #wwx = {'form':UsersForm(request.POST or {})}
	if request.method == "POST":
		try:
			form = UsersForm(request.POST)

			if form.is_valid():
	
				n = form.save(commit=False)
				n.createdTime = datetime.datetime.now()
				n.save()	
				#print request.POST
				return HttpResponse(n.firstName+"has been created!")
			else:
					
				return HttpResponse("has been created!")
		except Exception as e:
			return HttpResponse(e.args)
			
	else:
		form = UsersForm()
	return render(request, 'schoolLand/signUp.html', {"form":form,})

