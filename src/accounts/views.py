from django.shortcuts import render
from .forms import RegistrationForm,LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Profile
from django.urls import reverse
from django.contrib.auth.decorators import login_required
#from django.core.urlresolvers import reverse


from django.contrib.auth import (

	authenticate,
	login,
	logout

	)

def loginview(request):
	form = LoginForm(request.POST or None)
	if request.method =="POST":
		if form.is_valid():
			username = form.cleaned_data.get("username")
			password = form.cleaned_data.get("password")
			print(username,password)
			user = authenticate(username=username, password=password)
			login(request, user)
			return HttpResponseRedirect(reverse("home"))

	context = {
		'form':form 
	}
	return render(request, 'accounts/login.html', context)


@login_required
def logoutview(request):
	logout(request)
	return HttpResponseRedirect(reverse('home'))


def func(request):
	return render(request,'accounts/index.html')

def registerview(request):
	form = RegistrationForm(request.POST or None)
	
	if request.method=="POST":
	
		if form.is_valid():
			first_name = form.cleaned_data.get('first_name')
			last_name= form.cleaned_data.get('last_name')
			reg = form.cleaned_data.get("reg")
			mobile = form.cleaned_data.get("mobile")
			gender = form.cleaned_data.get("gender")
			dob = form.cleaned_data.get("dob")
			email = form.cleaned_data.get('email')
			username = form.cleaned_data.get("username")
			password  = form.cleaned_data.get('password ')
			cpassword  = form.cleaned_data.get('cpassword ')
			print(password)
			print(form.cleaned_data['password'])
			user, create = User.objects.get_or_create(
			
				first_name=first_name,
				last_name=last_name,
				username=username,
				email=email,

			)
			user.set_password(form.cleaned_data['password'])
			print(password)
			user.save()
			

			pro = Profile(reg=reg, mobile=mobile, dob=dob, gender=gender, user=user)
			pro.save()

			messages.success(request, "Successfully Saved")
		
			
			return render(request,'accounts/index.html')
	context = {
		'form':form,
	}
	return render(request, 'accounts/registration.html', context)

