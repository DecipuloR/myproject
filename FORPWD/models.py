from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Applicants(models.Model):

    DISABILITY_CATEGORIES = (
    ('Psychosocial Disability','psychosocial disability'),
    ('Chronic Illness', 'chronic illness'),
    ('Learning Disability', 'learning disability'),
    ('Mental Disability', 'mental disability'),
    ('Visual Disability','visual disability'),
    ('Orthopedic Disability','orthopedic disability'),
    ('Communication Disability','communication disability'),
    )

    Gender = (('Male','male'),('Female','female'),
        )

    firstName = models.CharField(max_length=100, default=None,null=True)
    lastName = models.CharField(max_length=100, default=None, null=True)
    middleName = models.CharField(max_length=100, default=None, null=True)
    disability = models.CharField(max_length=200, null=True ,choices= DISABILITY_CATEGORIES,)
    Address = models.CharField(max_length=100, blank=True, null=True)
    Age = models.IntegerField(default=0, null=True)
    Gender = models.CharField(null=True, max_length=100, choices=Gender)
    ContactNumber = models.CharField(max_length=100, null=True)
    BirthDate = models.DateField(default=None, null=True)
    DateUpdated = models.DateField(default=None,null=True)
    File = models.ImageField(upload_to='media', null=True)
    COIFile = models.FileField(upload_to='media', null=True)
    MCFile = models.FileField(upload_to='media', null=True)

    applicationResult = (('Approved','approved'),('Denied','denied'),)

    status = models.CharField(max_length = 100, null=True, default="Pending", choices=applicationResult)

    Pwdnumber = models.CharField(max_length=12, default="Pending")

    Check = (('Received','received'),('',''),)

    
    cash = models.CharField(max_length=100, null=True, default="Blank", choices= Check)


    class Meta:
        db_table = "Applicants info."
    def __str__(self):
        return self.firstName 


class React(models.Model):

    email = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    date = models.DateField(auto_now=True, null=True)
    message = models.TextField(null=True, default=None)

    def __str__(self): 
        return self.username

class Post(models.Model):
    
    PostAnnouncement = models.TextField(null=True, default='No Announcement yet.')

    class Meta:
        db_table = "POST"

    def __str__(self):
        return self.Post





    
