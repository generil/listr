from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login

from .models import Person
from .models import Question
from .models import Answer
from .models import Topic

def index(request):
    return render(request, 'home.html')

def login_view(request):
    if request.user.is_authenticated:
        print "stage 1 check"
        return redirect('topics')
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print "stage 2 check"
        if user is not None:
            print "stage 3 check"
            login(request, user)
            return redirect('topics')
        else:
            print "stage 4 check"
            context['error_message'] = 'Wrong username or password'
            context['username'] = username
    return render(request, 'home.html', context=context)

def questions(request):
    questions_list = Question.objects.all()
    context = {'questions': questions_list}
    return render(request, 'questions_page.html', context)

def question_detail(request, question_id):
    question = Question.objects.get(id = question_id)
    all_answers = Answer.objects.filter(question = question)
    html = "<h1>" + str(question) + "</h1></br><h2>" + question.details + "</h2><br>"
    for answer in all_answers:
        print answer.respondent
        html += "<h3>" + answer.answer + " by " + str(answer.respondent) + "<h3><br>"
    return HttpResponse(html)

def topics(request):
    topics_list = Topic.objects.all()
    context = {'topics': topics_list}
    return render(request, 'topics_page.html', context)

def topic_detail(request, topic_id):
    topic = Topic.objects.get(id = topic_id)
    all_questions = Question.objects.filter(topic = topic)
    html = "<h1>" + str(topic) + "</h1></br><h2>" + topic.details + "</h2><br>"
    for question in all_questions:
        url = '/questions/' + str(question.id) + '/'
        html += "<h3><a href = '" + url + "'>" + question.question + " </a> by " + str(question.questioner) + "<h3><br>"
    return HttpResponse(html)
