from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	mobile = models.CharField(max_length=13)
	reg = models.CharField(max_length=10)
	dob = models.DateField(auto_now=False, auto_now_add=False)
	gender = models.CharField(max_length=6)
	date_created = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
	

	def __str__(self):
		return self.mobile

	def __unicode__(self):
		return self.mobile

