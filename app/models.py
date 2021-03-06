from __future__ import unicode_literals

from django.db import models
#Create your models here.

class Year(models.Model):
	y_id		=	models.AutoField(primary_key=True)
	year		=	models.CharField(max_length=50,unique=True)
	total		=	models.IntegerField()
	comp		=	models.IntegerField()
	it			=	models.IntegerField()
	entc		=	models.IntegerField()
	total_placed=	models.IntegerField(null=True,blank=True)
	comp_placed	=	models.IntegerField(null=True,blank=True)
	it_placed	=	models.IntegerField(null=True,blank=True)
	entc_placed	=	models.IntegerField(null=True,blank=True)

	def __str__(self):
		return  self.year

class Company(models.Model):

	c_id		=	models.AutoField(primary_key=True)
	name		=	models.CharField(max_length=40)
	be_criteria	=	models.FloatField(blank=True,null=True)
	me_criteria	=	models.FloatField(blank=True,null=True)
	back		=	models.CharField(max_length=100,blank=True,null=True) ## 1. No Criteria 2. Active not Allowed 3. Passive not allowed
	position    =   models.CharField(max_length=30,null=True,blank=True)
	salary      =   models.FloatField(blank=True, null=True)
	ppt_date	=	models.DateTimeField(null=True,blank=True)
	hired_count = 	models.IntegerField(null=True,blank=True)
	other_details=	models.CharField(max_length=1000,null=True,blank=True)
	placed_url =	models.CharField(max_length=500, null=True, blank=True)
	reg_start	=	models.DateTimeField(null=True,blank=True)
	reg_end		=	models.DateTimeField(null=True,blank=True)
	reg_link	=	models.CharField(max_length=1000,null=True,blank=True)
	status 		=	models.CharField(max_length=50,null=True,blank=True)
	lock 		=	models.BooleanField(default=False)
	y_id		=	models.ForeignKey(Year,null=True,blank=True, on_delete=models.DO_NOTHING)							#foreign key to year table
	applied_students=	models.ManyToManyField('Student',blank=True)									#student can apply to many companies and a company can have many students
	hidden		=	models.BooleanField(default=False)
	code_name	=	models.CharField(max_length=20,null=True,blank=True)

	def __str__(self):
		if self.position:
			return  self.name + "("+ self.position + ")"
		else:
			return  self.name

class Student(models.Model):

	s_id		=		models.AutoField(primary_key=True)
	college_id	=		models.CharField(max_length=100,unique=True)
	roll		= 		models.CharField(max_length=100,unique=True)
	name        =		models.CharField(max_length=100)
	email       =		models.EmailField(max_length=100,unique=True)
	password    =		models.CharField(max_length=100)
	phone       =		models.CharField(max_length=100)
	gender      =		models.CharField(max_length=100)
	y_id        =		models.ForeignKey(Year, on_delete=models.DO_NOTHING)            												 #foreign key to year table
	branch		=		models.CharField(max_length=100)

	prn			=		models.CharField(max_length=500,unique=True,null=True,blank=True)
	birth_date	=		models.DateField(null=True,blank=True)
	per_address =		models.CharField(max_length=1000,null=True,blank=True)
	cur_address =		models.CharField(max_length=1000,null=True,blank=True)
	city		=		models.CharField(max_length=100,null=True,blank=True)
	aadhar_number=		models.CharField(max_length=500,null=True,blank=True)
	pan_number	 =		models.CharField(max_length=500,null=True,blank=True)
	passport_number=	models.CharField(max_length=500,null=True,blank=True)
	

	tenth_board =		models.CharField(max_length=500,null=True,blank=True)
	tenth_marks	=		models.FloatField(null=True,blank=True)
	tenth_schoolname=	models.CharField(max_length=1000,null=True,blank=True)
	tenth_city	=		models.CharField(max_length=500,null=True,blank=True)
	tenth_yeargap =  	models.BooleanField(default=False)
	tenth_yeargap_reason=models.CharField(max_length=1000,null=True,blank=True)

	is_diploma	  =		models.BooleanField(default=False)

	twelveth_board= 	models.CharField(max_length=500,null=True,blank=True)
	twelveth_year = 	models.CharField(max_length=100,null=True,blank=True)
	twelveth_marks=		models.FloatField(null=True,blank=True)
	twelveth_schoolname=models.CharField(max_length=1000,null=True,blank=True)
	twelveth_city	=	models.CharField(max_length=500,null=True,blank=True)
	twelveth_yeargap=	models.BooleanField(default=False)
	twelveth_yeargap_reason=models.CharField(max_length=1000,null=True,blank=True)

	diploma_board = 	models.CharField(max_length=500,null=True,blank=True)
	diploma_marks =		models.FloatField(null=True,blank=True)
	diploma_outof =		models.FloatField(null=True,blank=True)
	diploma_year  = 	models.CharField(max_length=100,null=True,blank=True)

	cgpi		  =		models.FloatField(null=True,blank=True)
	average		  =		models.FloatField(null=True,blank=True)
	active_back	 =		models.IntegerField(default=0)
	passive_back = 		models.BooleanField(default=False)

	#ME students
	course = models.CharField(max_length=10, null=True, blank=True, default="BE")
	me_fy_marks = models.FloatField(null=True,blank=True)
	me_sy_marks = models.FloatField(null=True,blank=True)
	be_collegename = models.CharField(max_length=1000,null=True,blank=True)
	be_university = models.CharField(max_length=1000,null=True,blank=True)
	be_passing_year = models.CharField(max_length=100,null=True,blank=True)
	be_yeargap = models.BooleanField(default=False)
	be_yeargap_reason = models.CharField(max_length=1000,null=True,blank=True)

	placed		=		models.BooleanField(default=False)
	url			=		models.CharField(max_length=500,null=True,blank=True)
	c_id		=		models.ForeignKey(Company,on_delete=models.SET_NULL,null=True,blank=True)			#foreign key o company table
	lock		=		models.BooleanField(default=False)
	update_marks =   	models.IntegerField(default=0)  ### option to be opened after results
						# 0 - option closed
						# 1 - update last year marks
						# 2 - update current sems marks

	def __str__(self):
		return  self.name

class Admin(models.Model):
	name		  =	models.CharField(max_length=50)
	email		  =	models.EmailField(max_length=60,unique=True)
	password	  =	models.CharField(max_length=12)
	other_details =	models.CharField(max_length=1000,null=True,blank=True)

	def __str__(self):
		return  self.name


class Verify(models.Model):
	v_id		=	models.AutoField(primary_key=True)
	prn			=	models.CharField(max_length=50)
	college_id  =   models.CharField(max_length=20)

	def __str__(self):
		return self.prn

class Message(models.Model):
	msg_id		=	models.AutoField(primary_key=True)
	timestamp 	=	models.DateTimeField()
	important 	=	models.BooleanField(default=False)
	title		=	models.CharField(max_length=200,default="")
	message		=	models.CharField(max_length=10000,default="",null=True,blank=True)
	url			=	models.CharField(max_length=50,null=True,blank=True)

	def __str__(self):
		return self.title

class Result(models.Model):
	r_id		=	models.AutoField(primary_key=True)
	c_id		=	models.ForeignKey(Company,on_delete=models.SET_NULL,null=True)			#foreign key o company table
	shortlist 	=	models.CharField(max_length=100)
	filename	=	models.CharField(max_length=100)
	url 		=	models.CharField(max_length=100)
	other_details= models.CharField(max_length=1000)

	def __str__(self):
		return self.filename
