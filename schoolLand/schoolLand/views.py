from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.template import RequestContext
from django.http import Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from schoolLand.forms import UsersForm
from django.contrib.auth.models import User
from schoolLand.models import messages
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#from schoolLand import models
import datetime
#from django import forms 
#from django.forms.models import modelformset_factory
# Create your views here.



def index(request):
	return render(request, 'schoolLand/index.html')

def signIn(request):
        #redirect to home page if it is user
        if request.user.is_authenticated():
                return redirect('/')
        if request.method == "POST":
                email    = request.POST['email']
                password = request.POST['password']
                user = authenticate(email=email, password=password)
                if user is not None:
                        if user.is_active:
                                login(request, user)
                                return redirect('/')
                        else:
                                return HttpResponse("account is disable")
                else:
                        return HttpResponse("Invalid login")
        else:
                form = UsersForm()
        return render(request, 'schoolLand/signIn.html', {"form":form,})

@login_required(login_url='/')
def signOut(request):
        if not request.user.is_authenticated():
                return redirect('/')
        else:
                #return HttpResponse("logged in user: "+request.user.first_name)
                logout(request)
                return redirect('/?next=%s' % request.path)

def signUp(request):
	#UsersFormSet = modelformset_factory(Users)
	#if(request.POST):
        #wwx = {'form':UsersForm(request.POST or {})}

        #redirect to home page if it is user
        if request.user.is_authenticated():
                return redirect('/')
	if request.method == "POST":
                if User.objects.filter(email = request.POST['email']).exists():
                        return HttpResponse("Email Address: "+ request.POST['email'] + " has existed. Please try to sign Up With another Email Address")
                else:
                        try:
                                form = UsersForm(request.POST)

                                if form.is_valid():
										
                                        n = form.save(commit=False)
					n.username = n.first_name + n.last_name
					n.set_password(n.password)
                                        #n.createdTime = datetime.datetime.now()
										#n.username = n.first_name
                                        n.save()
                                        user = authenticate(email=request.POST['email'], password=request.POST['password'])
                                        login(request, user)
                                        return redirect('/?next=%s' % request.path)
                                        #print request.POST
                                        #return HttpResponse(n.first_name+"has been created!")
                                else:
                                                
                                        return render(request, 'schoolLand/signUp.html', {"form":form,})
                        except Exception as e:
                                return HttpResponse(e.args)
			
	else:
		form = UsersForm()
	return render(request, 'schoolLand/signUp.html', {"form":form,})

@login_required(login_url='/')
def message(request):
        if request.method == "POST":
                if request.POST['message'] != "":
                        m = messages(message=request.POST['message'],user_id=request.user.id)
                        m.save()
                #return HttpResponse("test")
        lastWeek = timezone.now() - datetime.timedelta(days=30)
        last_week_messages = messages.objects.filter(createdTime__gte=lastWeek)
        return render_to_response('schoolLand/messages.html',{"messages":last_week_messages,},context_instance=RequestContext(request))
        #return render(request, 'schoolLand/messages.html', {"messages":last_week_messages,})

