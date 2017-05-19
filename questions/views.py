from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from datetime import tzinfo, timedelta, datetime
from django.conf import settings
from django.core.files.storage import FileSystemStorage


from .models import Person
from .models import Question
from .models import Answer
from .models import Topic
from .models import Instruction
from .models import Comment

# functions for the date

ZERO = timedelta(0)
# we have to settle for this for now
nameArray = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
			'11', '12', '13', '14', '15', '16', '17', '18', '19', '20']

class UTC(tzinfo):
	def utcoffset(self, dt):
		return ZERO

	def tzname(self, dt):
		return "UTC"

	def dst(self, dt):
		return ZERO


def prettydate(d):
	utc = UTC()
	diff = datetime.now(utc) - d
	s = diff.seconds
	if diff.days > 7 or diff.days < 0:
		return d.strftime('%b %d, %y')
	elif diff.days == 1:
		return '1 day ago'
	elif diff.days > 1:
		return '{} days ago'.format(diff.days)
	elif s <= 1:
		return 'just now'
	elif s < 60:
		return '{} seconds ago'.format(s)
	elif s < 120:
		return '1 minute ago'
	elif s < 3600:
		return '{} minutes ago'.format(s/60)
	elif s < 7200:
		return '1 hour ago'
	else:
		return '{} hours ago'.format(s/3600)

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
	if not request.user.is_authenticated:
		return redirect('/')
	questions_list = Question.objects.all()
	answers_count = []
	date_relative = []
	# number of answers in the question
	for question in questions_list:
		ans = Answer.objects.filter(question = question).count()
		question.ans_count = ans

	for item in questions_list:
		if isinstance(item.question_date, datetime):
			tmp = prettydate(item.question_date)
		else:
			tmp = "No date specified"

		date_relative.append(tmp)

	zipped_data = zip(questions_list, date_relative)

	context = {
		'questions': zipped_data
	}
	return render(request, 'questions.html', context)

def question_detail(request, question_id):
	if not request.user.is_authenticated:
		return redirect('/')
	question = Question.objects.get(id = question_id)
	all_answers = Answer.objects.filter(question = question)
	date = prettydate(question.question_date)
	date_relative = []
	# instructions = []
	for item in all_answers:
		item.answers = Instruction.objects.filter(answer = item)
		# print len(item.answers)
		if isinstance(item.answer_date, datetime):
			tmp = prettydate(item.answer_date)
		else:
			tmp = "No date specified"
		date_relative.append(tmp)

	zipped_data = zip(all_answers, date_relative)

	context = {
		'question': question,
		'answers': zipped_data,
		'question_date': date
	}
	return render(request, 'question_select.html', context)

def topics(request):
	if not request.user.is_authenticated:
		return redirect('/')
	topics_list = Topic.objects.all()
	for topic in topics_list:
		que = Question.objects.filter(topic = topic).count()
		topic.question_count = que
	context = {'topics': topics_list}
	return render(request, 'topics.html', context)

def topic_detail(request, topic_id):
	if not request.user.is_authenticated:
		return redirect('/')
	topic = Topic.objects.get(id = topic_id)
	all_questions = Question.objects.filter(topic = topic)
	date_relative = []
	for question in all_questions:
		ans = Answer.objects.filter(question = question).count()
		question.ans_count = ans

	for item in all_questions:
		if isinstance(item.question_date, datetime):
			tmp = prettydate(item.question_date)
		else:
			tmp = "No date specified"

		date_relative.append(tmp)

	zipped_data = zip(all_questions, date_relative)

	context = {
		'topic': topic,
		'questions': zipped_data,
	}
	return render(request, 'topic_select.html', context)

def answer(request, answer_id):
	if not request.user.is_authenticated:
		return redirect('/')
	question = Question.objects.get(id = question_id)
	answer = Answer.objects.get(pk = answer_id)
	comments = Comment.objects.filter(answer = answer)
	context = {
		'answer': answer,
		'comments': comments,
		'question': question
	}
	return render(request, 'answer.html', context)

def addquestion(request, topic_id):
	if not request.user.is_authenticated:
		return redirect('/')
	if request.method == 'POST':
		topic = Topic.objects.get(pk = topic_id)
		question = request.POST.get('question')
		details = request.POST.get('description')
		user = request.user
		Question.objects.create(question = question, details = details, questioner = user, topic = topic)
	return redirect('topic_detail', topic_id)

def addanswer(request, question_id):
	if not request.user.is_authenticated:
		return redirect('/')
	if request.method == 'POST':
		question = Question.objects.get(pk = question_id)
		description = request.POST.get('description')
		answers = []
		i = 0

		while request.POST.get(nameArray[i]) != None:
			answer = request.POST.get(nameArray[i])
			print i, answer
			answers.append(answer)
			i += 1

		a = Answer.objects.create(description = description, question = question, respondent = request.user)
		a.save()

		ai = 0
		for answer in answers:
			Instruction.objects.create(instruction = answer, answer = a, number = ai)
			ai += 1

	return redirect('question_detail', question_id)

def addtopic(request):
	if not request.user.is_authenticated:
		return redirect('/')
	if request.method == 'POST':
		topic = request.POST['topic']
		details = request.POST['details']
		creator = request.user

		topic_image = request.FILES['topic_file']
		fs = FileSystemStorage()
		topic_image.name = 'topic_' + topic + '_' + topic_image.name
		filename = fs.save(topic_image.name, topic_image)

		Topic.objects.create(topic = topic, details = details, creator = creator, image = filename)

	return redirect('topics')

def answer_detail(request, answer_id):
	if not request.user.is_authenticated:
		return redirect('/')
	answer = Answer.objects.get(id = answer_id)
	instructions = Instruction.objects.filter(answer = answer)
	comment_date = []
	date_relative = prettydate(answer.answer_date)
	comments = Comment.objects.filter(answer = answer)
	lencomments = len(comments)

	for item in comments:
		if isinstance(item.comment_date, datetime):
			tmp = prettydate(item.comment_date)
		else:
			tmp = "No date specified"

		comment_date.append(tmp)

	zipped_data = zip(comments, comment_date)

	context = {
		'answer': answer,
		'instructions': instructions,
		'date': date_relative,
		'comments': zipped_data,
		'lencomments': lencomments
	}
	return render(request, 'answer_select.html', context)

def addcomment(request, answer_id):
	if not request.user.is_authenticated:
		return redirect('/')
	if request.method == 'POST':
		answer = Answer.objects.get(id = answer_id)
		comment = request.POST['comment']
		commenter = request.user

		Comment.objects.create(comment = comment, answer = answer, commenter = commenter)

	return redirect('answer_detail', answer_id)

def answer_upvote(request, answer_id):
	if not request.user.is_authenticated:
		return redirect('/')
	redirect_url = request.GET.get('next')
	if request.method == 'POST':
		answer = Answer.objects.get(id = answer_id)
		answer.upvotes += 1
		answer.save()

	return redirect(redirect_url)

def answer_downvote(request, answer_id):
	if not request.user.is_authenticated:
		return redirect('/')
	redirect_url = request.GET.get('next')
	if request.method == 'POST':
		answer = Answer.objects.get(id = answer_id)
		answer.downvotes += 1
		answer.save()

	return redirect(redirect_url)

def question_upvote(request, question_id):
	if not request.user.is_authenticated:
		return redirect('/')
	redirect_url = request.GET.get('next')
	if request.method == 'POST':
		question = Question.objects.get(id = question_id)
		question.upvotes += 1
		question.save()

	return redirect(redirect_url)

def question_downvote(request, question_id):
	if not request.user.is_authenticated:
		return redirect('/')
	redirect_url = request.GET.get('next')
	if request.method == 'POST':
		question = Question.objects.get(id = question_id)
		question.downvotes += 1
		question.save()

	return redirect(redirect_url)

def profile(request, user_id):
	if not request.user.is_authenticated:
		return redirect('/')
	user = User.objects.get(id = user_id)
	questions = Question.objects.filter(questioner = user)
	answers = Answer.objects.filter(respondent = user)
	question_date = []
	answer_time = []
	
	for question in questions:
		ans = Answer.objects.filter(question = question).count()
		question.ans_count = ans

	for item in questions:
		if isinstance(item.question_date, datetime):
			tmp = prettydate(item.question_date)
		else:
			tmp = "No date specified"
		question_date.append(tmp)

	for item in answers:
		if isinstance(item.answer_date, datetime):
			tmp = prettydate(item.answer_date)
		else:
			tmp = "No date specified"
		answer_time.append(tmp)

	questions = zip(questions, question_date)
	answers = zip(answers, answer_time)

	context = {
		'user': user,
		'questions': questions,
		'answers': answers,
	}
	return render(request, 'profile.html', context)
