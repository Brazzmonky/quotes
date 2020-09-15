from __future__ import unicode_literals
from django.db import models
import re, bcrypt

class UserManager(models.Manager):
	def register_validator(self,postData):
		EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
		errors={}
		validemail=User.objects.filter(email=postData['email'])
		if len(validemail) > 0:
			errors['email']="Email already in use. Please login or choose another."
		if not EMAIL_REGEX.match(postData['email']):
			errors['emailtype']="Invalid email address!"
		if len(postData['user_name']) < 2:
			errors['user_name']="Required field, please input a Username of at least 2 characters."
		if len(postData['password']) < 8:
			errors['password']="Required field please choose a password of at least 8 characters."
		if postData['password'] != postData['confirmpw']:
			errors['confirmpw']= "Passwords must match."
		return errors

	def login_validator(self,postData):
		usermail=User.objects.filter(email=postData['email'])
		errors={}
		if len(postData['email']) ==0:
			errors['email']="Required field please enter a valid email."
		if len(usermail) < 1:
			errors['email']="No Email matching that address, please register or try another."
		else:
			user=User.objects.get(email=postData['email'])
			if bcrypt.checkpw(postData['password'].encode(),user.password.encode()):
				print("password match")
			else:
				errors['passwordfailed']="Incorrect password, please try again."
				print("failed password")
		return errors			

class User(models.Model):
	user_name=models.CharField(max_length=255)
	email=models.CharField(max_length=255)
	password=models.CharField(max_length=255)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	objects=UserManager()
	def __repr__(self):
		return f'User: {self.user_name} {self.email} ({self.created_at}) ({self.updated_at})'

class QuoteManager(models.Manager):
	def quote_validator(self,postData):
		errors={}
		if len(postData['content']) < 8:
			errors['content']="Required field, please add a quote of at least 8 characters."
		if len(postData['author']) < 3:
			errors['author']="Required field, please add an author."
		return errors

class Quote(models.Model):
	content=models.CharField(max_length=255)
	author=models.CharField(max_length=255)
	user=models.ForeignKey(User, related_name="quote",on_delete=models.CASCADE,default=None,null=True)
	favorite=models.ManyToManyField(User, related_name="quotes")
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	objects=QuoteManager()
	def __repr__(self):
		return f'Quote: {self.content} {self.author} {self.user}'



