from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

#User Model Extension

#class Teacher(models.Model):
#	user = models.OneToOneField(User)


#Main Models

class School(models.Model):
    name = models.CharField(max_length=100)

class Class(models.Model):
    name = models.CharField(max_length=100)

class Badge(models.Model):
	badge_type = models.CharField(max_length=20)

class Merit(models.Model):
	name = models.CharField(max_length=100)
	points = models.IntegerField()
	timestamp = models.DateTimeField()
	merit_type = models.ForeignKey('MeritType')

class MeritType(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=100)

class Message(models.Model):
	from_user = models.ForeignKey(User,related_name='message_from_user')
	to_user = models.ForeignKey(User,related_name='message_to_user')

admin.site.register(School)
admin.site.register(Class)
admin.site.register(Badge)
admin.site.register(Merit)
admin.site.register(MeritType)
admin.site.register(Message)