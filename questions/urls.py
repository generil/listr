from django.conf.urls import url
from . import views

urlpatterns = [
	# /signup/
  url(r'^$', views.index, name='index'),
  # /questions/
  url(r'^questions/$', views.questions, name='questions'),
  # /qustions/id
  url(r'^questions/(?P<question_id>[0-9]+)/$', views.question_detail, name='question_detail'),
]
