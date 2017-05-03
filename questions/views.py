from django.http import HttpResponse

def index(request):
	return HttpResponse("<h1> Welcome to Listr.io's Question pages! </h1>")