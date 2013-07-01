from django.template.loader import get_template
from django.template import Context, RequestContext
from django.http import HttpResponse
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
	html = t.render(Context({'variable1':'Dashboard'}))
	return HttpResponse(html)

def sign_in(request):
	if request.method == 'GET':
		t = get_template('sign_in.html')
		html = t.render(RequestContext(request))
		return HttpResponse(html)
	elif request.method == 'POST':
		t = get_template('sign_in.html')
		html = t.render(RequestContext(request))
		return HttpResponse(html)

		# username = request.POST['username']
  #   	password = request.POST['password']
  #   	user = authenticate(username=username, password=password)
  #   	if user is not None:
		# 	if user.is_active:
		# 		login(request, user)