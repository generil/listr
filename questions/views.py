from django.http import HttpResponse
from django.shortcuts import render
from models import User
from models import Question
from models import Answer

def index(request):
  return render(request, 'home.html')

def questions(request):
	all_questions = Question.objects.all()
	html = "<h1> Questions by the Community</h1></br>"
	for question in all_questions:
		url = '/questions/' + str(question.id) +'/'
		html += "<h3><a href = '" + url + "'>" + question.question + " </a> by " + str(question.user_id) + "<h3><br>"
	return HttpResponse(html)	

def question_detail(request, question_id):
	question = Question.objects.get(id = question_id)
	all_answers = Answer.objects.filter(question = question)
	html = "<h1>" + str(question) + "</h1></br><h2>" + question.details + "</h2><br>"
	for answer in all_answers:
		html += "<h3>" + answer.answer + " by " + str(answer.user_id) + "<h3><br>"
	return HttpResponse(html)	