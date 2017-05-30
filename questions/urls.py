from django.conf.urls import url
from . import views

urlpatterns = [
	# /signup/
  url(r'^$', views.index, name='index'),
  # /login/
  url(r'^login/$', views.login_view, name='login'),
  # /signup/
  url(r'^signup/$', views.signup_view, name='signup'),
  # /logout/
  url(r'^logout/$', views.logout_view, name='logout'),
  # /questions/
  url(r'^questions/$', views.questions, name='questions'),
  # /qustions/id
  url(r'^questions/(?P<question_id>[0-9]+)/$', views.question_detail, name='question_detail'),
  # /topics/
  url(r'^topics/$', views.topics, name='topics'),
  # /qustions/id
  url(r'^topics/(?P<topic_id>[0-9]+)/$', views.topic_detail, name='topic_detail'),
  # /addquestion/
  url(r'^addquestion/(?P<topic_id>[0-9]+)/$', views.addquestion, name='addquestion'),
  # /addquestion/
  url(r'^addquestion_by_topic/$', views.addquestion_by_topic, name='addquestion-select-topic'),
  # /answer/
  url(r'^answer/(?P<answer_id>[0-9]+)/$', views.answer_detail, name='answer_detail'),
  # /addanswer/
  url(r'^addanswer/(?P<question_id>[0-9]+)/$', views.addanswer, name='addanswer'),
  # /addtopic/
  url(r'^addtopic/$', views.addtopic, name='addtopic'),
  # /addcomment/
  url(r'^addcomment/(?P<answer_id>[0-9]+)/$', views.addcomment, name='addcomment'),
  # /answerupvote/
  url(r'^answer_upvote/(?P<answer_id>[0-9]+)/$', views.answer_upvote, name='answer_upvote'),
  # /answerdownvote/
  url(r'^answer_downvote/(?P<answer_id>[0-9]+)/$', views.answer_downvote, name='answer_downvote'),
  # /questionupvote/
  url(r'^question_upvote/(?P<question_id>[0-9]+)/$', views.question_upvote, name='question_upvote'),
  # /questiondownvote/
  url(r'^question_downvote/(?P<question_id>[0-9]+)/$', views.question_downvote, name='question_downvote'),
  # /profile/
  url(r'^profile/(?P<user_id>[0-9]+)/$', views.profile, name='profile'),
  # /likecomment/
  url(r'^likecomment/(?P<comment_id>[0-9]+)/$', views.likecomment, name='likecomment'),
  # /edit_profile_view/
  url(r'^edit_profile_view/$', views.edit_profile_view, name='edit_profile_view'),
  # /edit_profile_view/
  url(r'^edit_profile/$', views.edit_profile, name='edit_profile'),
  # /delete_question/
  url(r'^delete_question/(?P<question_id>[0-9]+)/$', views.delete_question, name='delete_question'),
  url(r'^delete_answer/(?P<answer_id>[0-9]+)/$', views.delete_answer, name='delete_answer'),
  url(r'^delete_comment/(?P<comment_id>[0-9]+)/$', views.delete_comment, name='delete_comment')
]