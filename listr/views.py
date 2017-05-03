from django.http import HttpResponse

def index(request):
	return HttpResponse("<h1> Welcome to Listr.io </h1>")

def login(request):
	return HttpResponse("<h1> Login to Listr.io </h1>")