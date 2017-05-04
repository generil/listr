from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	# return HttpResponse("<h1> Welcome to Listr.io </h1>"
	return render(request, "index.html", context=None)

def login(request):
	return HttpResponse("<h1> Login to Listr.io </h1>")

def signup(request):
	return HttpResponse("<h1> Signup to Listr.io </h1>")
