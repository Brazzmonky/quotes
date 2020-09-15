from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
import bcrypt

def loginpage(request):
	return render(request, 'login.html')


def newUser(request):
	errors=User.objects.register_validator(request.POST)
	if len(errors) > 0:
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('/')
	else:
		password=request.POST['password']
		pw_hash=bcrypt.hashpw(password.encode(), bcrypt.gensalt())
		newUser=User.objects.create(user_name=request.POST['user_name'],email=request.POST['email'],password=pw_hash.decode())		
		request.session['loggedinUserID'] = newUser.id
		return redirect('/Success')


def login(request):
	errors=User.objects.login_validator(request.POST)
	if len(errors) >0:
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('/')
	else:
		loggedinUser=User.objects.get(email=request.POST['email'])		
		request.session['loggedinUserID'] = loggedinUser.id
		return redirect('/Success')


def home(request):
	all_quotes=Quote.objects.all()
	loggedinUser= User.objects.get(id=request.session['loggedinUserID'])
	context={
	"all_quotes":all_quotes,
	"loggedinUser":loggedinUser,
	}
	return render(request, 'home.html',context)


def Success(request):
	loggedinUser= User.objects.get(id=request.session['loggedinUserID'])
	context={
	"loggedinUser":loggedinUser,
	}
	return render(request, 'Success.html',context)

def makequote(request):
	errors=Quote.objects.quote_validator(request.POST)
	loggedinUser= User.objects.get(id=request.session['loggedinUserID'])
	if len(errors) > 0:
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('/home')
	else:
		loggedinUser= User.objects.get(id=request.session['loggedinUserID'])
		Quote.objects.create(content=request.POST['content'],author=request.POST['author'],user=loggedinUser)	
		return redirect('/home')

def edit(request,quoteid):
	quote_to_edit=Quote.objects.get(id=quoteid)
	context={
	"quote_to_edit":quote_to_edit,
	}
	return render(request, 'edit.html',context)

def editquote(request,quoteid):
	errors=Quote.objects.quote_validator(request.POST)
	if len(errors) > 0:
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('/edit/'+str(quoteid))
	else:
		loggedinUser= User.objects.get(id=request.session['loggedinUserID'])		
		quote_to_edit=Quote.objects.get(id=quoteid)
		context={
		"quote_to_edit":quote_to_edit,
		"loggedinUser":loggedinUser,
		}
		quote_to_edit.content=request.POST['content']
		quote_to_edit.author=request.POST['author']
		quote_to_edit.save()	
		return redirect('/home', context)

def stats(request,userid):
	user_to_display=User.objects.get(id=userid)
	user_quotes=Quote.objects.filter(user=User.objects.get(id=userid))
	content={
	"user_quotes": user_quotes,
	"user_to_display":user_to_display,
	}
	return render(request, 'stats.html', content)

def boop(request,quoteid):
	quote_to_delete=Quote.objects.get(id=quoteid)
	quote_to_delete.delete()
	return redirect('/home')

def logout(request):
	request.session.clear()
	return redirect('/')

def addfavorite(request,quoteid):
	quote_to_favorite=Quote.objects.get(id=quoteid)
	loggedinUser= User.objects.get(id=request.session['loggedinUserID'])
	quote_to_favorite.favorite.add(loggedinUser)
	return redirect('/home')

