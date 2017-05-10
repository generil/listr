from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .models import Person
from .models import Question
from .models import Answer
from .models import Topic

def index(request):
	return render(request, 'home.html')

def login_view(request):
	if request.user.is_authenticated:
		return redirect('questions')
	context = {}
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('questions')
		else:
			context['error_message'] = 'Invalid Username or Password'
			context['username'] = username
	return render(request, 'home.html', context=context)

def signup_view(request):
	if request.user.is_authenticated:
		return redirect('questions')
	context = {}
	data = {}
	if request.method == 'POST':
		data['first_name'] = request.POST.get('first_name')
		data['last_name'] = request.POST.get('last_name')
		data['username'] = request.POST.get('username')
		data['email'] = request.POST.get('email')
		data['password1'] = request.POST.get('password1')
		data['password2'] = request.POST.get('password2')

		dataCheck = user_integrityCheck(data)
		if dataCheck == True:
			User.objects.get_or_create(first_name = data['first_name'],
				last_name = data['last_name'], username = data['username'], password = data['password1'],
				email = data['email'])
			user_auth = authenticate(username=data['username'], password=['password1'])
			print user
			login(request, user_auth)
			return redirect('questions')
		else:
			context = dataCheck[1]

	return render(request, 'home.html', context=context)

def user_integrityCheck(data):
	errors = {}

	if len(User.objects.filter(username = data.get('username'))) > 0:
		errors['username_error'] = "An account has this Username already. Pick another one."
		return False, errors
	if len(User.objects.filter(email = data.get('email'))) > 0:
		errors['email_error'] = "An account has this Email already. Pick another one."
		return False, errors
	if data.get('password1') != data.get('password2'):
		errors['password_error'] = "Passwords do not match"

	return True

def logout_view(request):
  logout(request)
  return redirect('index')

def questions(request):
	questions_list = Question.objects.all()
	answers_count = []
	for question in questions_list:
		ans = Answer.objects.filter(question = question).count()
		question.ans_count = ans
	context = {
		'questions': questions_list
	}
	return render(request, 'questions_page.html', context)

def question_detail(request, question_id):
	question = Question.objects.get(id = question_id)
	all_answers = Answer.objects.filter(question = question)
	context = {
		'question': question,
		'answers': all_answers
	}
	return render(request, 'chosen_question.html', context)

def topics(request):
	topics_list = Topic.objects.all()
	for topic in topics_list:
		que = Question.objects.filter(topic = topic).count()
		topic.question_count = que
	context = {'topics': topics_list}
	return render(request, 'topics_page.html', context)

def topic_detail(request, topic_id):
	topic = Topic.objects.get(id = topic_id)
	all_questions = Question.objects.filter(topic = topic)
	for question in all_questions:
		ans = Answer.objects.filter(question = question).count()
		question.ans_count = ans
	context = {
		'topic': topic,
		'questions': all_questions,
	}
	return render(request, 'chosen_topic.html', context)

def addquestion(request, topic_id):
	if request.method == 'POST':
		topic = Topic.objects.get(pk = topic_id)
		question = request.POST.get('question')
		details = request.POST.get('description')
		user = request.user
		Question.objects.create(question = question, details = details, questioner = user, topic = topic)
	return redirect('topic_detail', topic_id)

def addanswer(request, question_id):
	if request.method == 'POST':
		question = Question.objects.get(pk = question_id)
		answer = request.POST.get('answerbaby')
		user = request.user
		print question
		print answer
		print user
		Answer.objects.create(answer = answer, question = question, respondent = user)
	return redirect('question_detail', question_id)