from django.shortcuts import render
from .forms import RegistrationForm,LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse
from .models import Profile
from .models import inputreviews
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt 
import numpy as np
import io
 
#from django.db import connection
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
			college = form.cleaned_data.get("college")
			#dob = form.cleaned_data.get("dob")
			email = form.cleaned_data.get('email')
			username = form.cleaned_data.get("username")
			password  = form.cleaned_data.get('password ')
			cpassword  = form.cleaned_data.get('cpassword ')
			
			user, create = User.objects.get_or_create(
			
				first_name=first_name,
				last_name=last_name,
				username=username,
				email=email,

			)
			user.set_password(form.cleaned_data['password'])
			user.save()
			

			pro = Profile(reg=reg, mobile=mobile, college=college , gender=gender, user=user)
			pro.save()

			messages.success(request, "Successfully Saved")
		
			
			return render(request,'accounts/index.html')
	context = {
		'form':form,
	}
	return render(request, 'accounts/registration.html', context)



def givereview(request,id):
	id=int(id)
	profile = Profile.objects.filter(user_id=id)
	profile=profile[0]
	#print(id)
	#print(profile.college)
	context = {
		'profile':profile.college,
	}
	return render(request,'accounts/review.html',context)


def reviewsview(request,colg):
	colg=str(colg)
	print(colg)
	if request.method == "POST":

		a1 = request.POST.get("a1")
		a2 = request.POST.get("a2")
		a3 = request.POST.get("a3")
		a4 = request.POST.get("a4")
		

		b1 = request.POST.get("b1")
		b2 = request.POST.get("b2")
		b3 = request.POST.get("b3")
		b4 = request.POST.get("b4")

		c1 = request.POST.get("c1")
		c2 = request.POST.get("c2")
		c3 = request.POST.get("c3")
		c4 = request.POST.get("c4")

		d1 = request.POST.get("d1")
		d2 = request.POST.get("d2")
		d3 = request.POST.get("d3")

		e1 = request.POST.get("e1")
		e2 = request.POST.get("e2")
		e3 = request.POST.get("e3")
		e4 = request.POST.get("e4")

		if  e1 == None :
			e1 = 0
		if  e2 == None :
			e2 = 0
		if  e3 == None :
			e3 = 0
		if  e4 == None :
			e4 = 0

		if  d1 == None :
			d1 = 0
		if  d2 == None :
			d2 = 0
		if  d3 == None :
			d3 = 0

		if  c1 == None :
			c1 = 0
		if  c2 == None :
			c2 = 0
		if  c3 == None :
			c3 = 0
		if  c4 == None :
			c4 = 0

		if  b1 == None :
			b1 = 0
		if  b2 == None :
			b2 = 0
		if  b3 == None :
			b3 = 0
		if  b4 == None :
			b4 = 0

		if  a1 == None :
			a1 = 0
		if  a2 == None :
			a2 = 0
		if  a3 == None :
			a3 = 0
		if  a4 == None :
			a4 = 0

		
		print(a1,a2,a3,a4)
		print(b1,b2,b3,b4)
		print(c1,c2,c3,c4)
		print(d1,d2,d3)
		print(e1,e2,e3,e4)
		review = inputreviews.objects.filter(college=colg)
		review = review[0]
		print(review.infrastructure,review.Academics)
		
		a1 = int(a1)
		a2 = int(a2)
		a3 = int(a3)
		a4 = int(a4)

		b1 = int(b1)
		b2 = int(b2)
		b3 = int(b3)
		b4 = int(b4)

		c1 = int(c1)
		c2 = int(c2)
		c3 = int(c3)
		c4 = int(c4)

		d1 = int(d1)
		d2 = int(d2)
		d3 = int(d3)
		#d4 = int(d4)

		e1 = int(e1)
		e2 = int(e2)
		e3 = int(e3)
		e4 = int(e4)

		infra = review.infrastructure+(a1+a2+a3+a4)/20*100
		academic = review.Academics+(b1+b2+b3+b4)/20*100
		curr = review.Curricular+(c1+c2+c3+c4)/20*100
		placement = review.Placement+(d1+d2+d3)/20*100
		hostel = review.Hostel+(e1+e2+e3+e4)/20*100

		n = review.No_of_reviews + 1
		avg = (infra + academic + curr + placement + hostel) / 5
		inputreviews.objects.filter(college=colg).update(infrastructure = infra, Academics = academic, Curricular = curr, Placement = placement, Hostel = hostel, No_of_reviews = n , Average = avg  )
	
	return render(request,'accounts/index.html')







def graphviews(request):

	pos = [0]*10
	neg = [0]*10

	all_data = inputreviews.objects.values_list('college', 'Average')
	print(all_data)
	for i in range(len(all_data)):
		if all_data[i][0] == 'NIT Agartala':
			pos[0] = all_data[i][1]
			neg[0] = 100 - all_data[i][1]

		elif all_data[i][0] == 'NIT Allahabad':
			pos[1] = all_data[i][1]
			neg[1] = 100 - all_data[i][1]

		elif all_data[i][0]== 'NIT Bhopal':
			pos[2] = all_data[i][1]
			neg[2] = 100 - all_data[i][1]

		elif all_data[i][0] == 'NIT Calicut':
			pos[3] = all_data[i][1]
			neg[3] = 100 - all_data[i][1]

		elif all_data[i][0] == 'NIT Jamshedpur':
			pos[4] = all_data[i][1]
			neg[4] = 100 - all_data[i][1]

		elif all_data[i][0] == 'NIT Kurukshetra':
			pos[5] = all_data[i][1]
			neg[5] = 100 - all_data[i][1]

		elif all_data[i][0] == 'NIT Raipur':
			pos[6] = all_data[i][1]
			neg[6] = 100 - all_data[i][1]

		elif all_data[i][0] == 'NIT Surathkal':
			pos[7] = all_data[i][1]
			neg[7] = 100 - all_data[i][1]

		elif all_data[i][0] == 'NIT Tiruchirappalli':
			pos[8] = all_data[i][1]
			neg[8] = 100 - all_data[i][1]

		elif all_data[i][0] == 'NIT Warangal':
			pos[9] = all_data[i][1]
			neg[9] = 100 - all_data[i][1]


	n = 10
	ind = np.arange(n)    # the x locations for the groups
	width = 0.55      # the width of the bars: can also be len(x) sequence

	
	fig, ax = plt.subplots()
	ax.bar(ind, pos, width,color='green')
	ax.bar(ind,neg,width,bottom=pos,color='red')
	ax.set(ylabel ='Level of measurement', title = 'Analysis of various NITs')
	ax.set_xticks(ind)
	ax.set_xticklabels(['NIT Agartala','NIT Allahabad','NIT Bhopal','NIT Calicut', 'NIT Jamshedpur', 'NIT Kurukshetra', 'NIT Raipur', 
		'NIT Surathkal','NIT Tiruchirappalli','NIT Warangal'])
	ax.set_xticks(ind,(	))
	ax.grid()

	FigureCanvas(fig)
	buf = io.BytesIO()
	plt.savefig(buf, format='png')
	plt.close(fig)
	response = HttpResponse(buf.getvalue(), content_type='image/png')
	return response







def graphsviews(request,colg):
	colg = str(colg)

	pos = [0]*5
	neg = [0]*5

	all_data = inputreviews.objects.filter(college=colg)
	all_data = all_data[0]
	#print(all_data)
	n = all_data.No_of_reviews
	pos[0] = all_data.infrastructure
	neg[0] = (n*20) - all_data.infrastructure


	pos[1] = all_data.Academics
	neg[1] = (n*20)- all_data.Academics


	pos[2] = all_data.Placement
	neg[2] = (n*20) - all_data.Placement

	pos[3] = all_data.Hostel
	neg[3] = (n*20)- all_data.Hostel

	pos[4] = all_data.Curricular
	neg[4] = (n*20) - all_data.Curricular


	n = 5
	ind = np.arange(n)    # the x locations for the groups
	width = 0.50      # the width of the bars: can also be len(x) sequence

	
	fig, ax = plt.subplots()
	ax.bar(ind, pos, width,color='green')
	ax.bar(ind,neg,width,bottom=pos,color='red')
	ax.set(ylabel ='Level of measurement', title = 'Analysis of '+colg)
	ax.set_xticks(ind)
	ax.set_xticklabels(['Infrastructure','Academics','Placements','Hostels', 'Extra-Curricular'])
	ax.set_xticks(ind,(	))
	ax.grid()

	FigureCanvas(fig)
	buf = io.BytesIO()
	plt.savefig(buf, format='png')
	plt.close(fig)
	response = HttpResponse(buf.getvalue(), content_type='image/png')
	return response

