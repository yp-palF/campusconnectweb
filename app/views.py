from django.shortcuts import render
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.http import *
from django.template import loader
from django.conf import settings
from django.conf.urls.static import static
import validate
from models import User
import json
# Create your views here.

@csrf_exempt
def signin(request):
	template = loader.get_template("signin.html")
	return HttpResponse(template.render())


@csrf_exempt
def start(request):
	gId=None
	if(request.method=="POST"):
		gId = request.POST["gId"]
	if(gId==None):
		return HttpResponseRedirect("/signin")
	try:
		User.objects.get(gprofileId=gId)
		#template = loader.get_template("home.html") #home
		return HttpResponseRedirect("/home")
	except:
		User.objects.create(gprofileId=gId)
		template = loader.get_template("login.html") #TODO: change name signup page
		return HttpResponse(template.render())

@csrf_exempt
def sign_up(request):
	#call the api
	template = loader.get_template("home.html")
	response = HttpResponseRedirect("/home")
	response.set_cookie("id","hi")
	return response

@csrf_exempt
def home(request):
	template = loader.get_template("home.html") #home
	return HttpResponse(template.render())
@csrf_exempt
def course_page(request):
	#course_id = QueryDict(request.META['QUERY_STRING'])["course_id"]
	template = loader.get_template("Courses.html")
	response = HttpResponse(template.render())
	#response.set_cookie()
	return HttpResponse(template.render())

@csrf_exempt
def notes_page(request):
	#note_id = QueryDict(request.META['QUERY_STRING'])["course_id"]
	template = loader.get_template("notes.html")
	response = HttpResponse(template.render())
	#response.set_cookie()
	return HttpResponse(template.render())

@csrf_exempt
def profile(request):
	template = loader.get_template("profile.html")
	return HttpResponse(template.render())

@csrf_exempt
def search_action(request):
	if(request.method=="POST"):
		return HttpResponseRedirect("/search")


@csrf_exempt
def search_page(request):
	template = loader.get_template("search.html")
	return HttpResponse(template.render())

@csrf_exempt
def upload_page(request):
	template = loader.get_template("uploads.html")
	return HttpResponse(template.render())










#gId = "test"
# @csrf_exempt
# def test(request):
# 	template = loader.get_template("uploads.html")
# 	return HttpResponse(template.render())
# @csrf_exempt
# def index(request):
# 	gId=None
# 	if(request.method=="POST"):
# 		gId = request.POST["gId"]
	

# 	# print(data)
# 	# template = loader.get_template("index.html")
# 	# request.session["sid"] = "123"
# 	# a = HttpResponse(template.render())
# 	# print request.COOKIES
# 	# User.objects.create(profileId=123)
# 	if(gId==None):
# 		return HttpResponseRedirect("/signin")

# 	try:
# 		User.objects.get(gprofileId=gId)
# 		template = loader.get_template("secondpage.html") #home
# 		return HttpResponse(template.render())
# 	except:
# 		User.objects.create(gprofileId=gId)
# 		template = loader.get_template("index.html") #signup
# 		return HttpResponse(template.render())

# @csrf_exempt
# def redirect(request):
# 	a=request.META['QUERY_STRING']
# 	print(request.COOKIES)
# 	Q = QueryDict(a)
# 	id = request.COOKIES["profileId"]	
# 	if(validate.validate(profileId=id,sessionId=request.session)):
# 		template = loader.get_template("secondpage.html")
# 		return HttpResponse(template.render())
# 	else:
# 		return HttpResponse("Fuck Off")

