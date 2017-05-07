from django.conf.urls import url
from . import views

urlpatterns = [
	# /signup/
  url(r'^$', views.index, name='index'),
  # /login/
  url(r'^login/$', views.login_view, name='login'),
  # /questions/
  url(r'^questions/$', views.questions, name='questions'),
  # /qustions/id
  url(r'^questions/(?P<question_id>[0-9]+)/$', views.question_detail, name='question_detail'),
  # /topics/
  url(r'^topics/$', views.topics, name='topics'),
   # /qustions/id
  url(r'^topics/(?P<topic_id>[0-9]+)/$', views.topic_detail, name='topic_detail'),
]
