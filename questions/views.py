from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'login.html')

def login(request):
    return HttpResponse("<h1>Logged in!</h1>")

def signup(request):
	return render(request, 'signup.html')
