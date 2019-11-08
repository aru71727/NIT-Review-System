from django.shortcuts import render
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Profile
#from django.core.urlresolvers import reverse

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

			user, create = User.objects.get_or_create(
			
				first_name=first_name,
				last_name=last_name,
				username=username,
				email=email,

			)
			user.set_password(password)
			user.save()

			pro = Profile(reg=reg, mobile=mobile, dob=dob, gender=gender, user=user)
			pro.save()

			messages.success(request, "Successfully Saved")
		
			
			return render(request,'accounts/index.html')
	context = {
		'form':form,
	}
	return render(request, 'accounts/registration.html', context)

