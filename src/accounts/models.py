from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	mobile = models.CharField(max_length=13)
	reg = models.CharField(max_length=10)
	college = models.CharField(max_length=30)
	gender = models.CharField(max_length=6)
	date_created = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
	rated = models.IntegerField(default=0)

	

	def __str__(self):
		return self.college

	def __unicode__(self):
		return self.college


class inputreviews(models.Model):
	college = models.CharField(max_length=30)
	infrastructure = models.IntegerField(default=0)
	Academics = models.IntegerField(default=0)
	Curricular = models.IntegerField(default=0)
	Placement = models.IntegerField(default=0)
	Hostel = models.IntegerField(default=0)
	No_of_reviews = models.IntegerField(default=0)
	Average = models.IntegerField(default=0)
	

	def __str__(self):
		return self.college
	

class Colleges(models.Model):
    colg_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to="accounts/images",default="")


    def __str__(self):
        return self.colg_name

