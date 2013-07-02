from django.template.loader import get_template
from django.contrib.auth.models import User, Permission
from django.template import Context, RequestContext
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
import datetime

def home(request):
    #now = datetime.datetime.now()
    #t = get_template('home.html')
    #html = t.render(Context({'current_date': now}))
    #html = t.render(Context())

    return home_logged_in(request)
    #return HttpResponse(html)

def home_logged_in(request):
	t = get_template('home.html')
	html = t.render(Context({'variable1':'Home'}))
	return HttpResponse(html)

def sign_in(request):
	if request.method == 'GET':
		t = get_template('sign_in.html')
		html = t.render(RequestContext(request))
		return HttpResponse(html)
	elif request.method == 'POST':
		try:
			#Need to test the below for empty fields
			email = request.POST['email']
			password = request.POST['password']

			user_by_email = User.objects.get(email=email) #not found to be caught below
			user = authenticate(username=user_by_email.username,password=password)
			login(request,user)

			if user is not None:
				return HttpResponseRedirect("/dashboard/")
			else:
				t = get_template('sign_in.html')
				html = t.render(RequestContext(request))
				return HttpResponse(html)
		except Exception, error:
			return HttpResponse(error)

		# username = request.POST['username']
  #   	password = request.POST['password']
  #   	user = authenticate(username=username, password=password)
  #   	if user is not None:
		# 	if user.is_active:
		# 		login(request, user)

def dashboard(request):
	if request.user.is_authenticated():
		t = get_template('dashboard.html')
		html = t.render(Context({'variable1':'Dashboard for '+request.user.username+'!'}))
		return HttpResponse(html)
	else:
		return HttpResponseRedirect('/signin/')


	