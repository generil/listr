from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

def instruction_image_uploadpath(instance, filename):
  return './storage/instructions/instr_{}_{}'.format(answer_id, filename)


class Person(models.Model):
	user = models.OneToOneField(User)

	institution = models.CharField(max_length = 30)
	position = models.CharField(max_length = 30)
	join_date = models.DateTimeField(auto_now_add=True)
	is_verified = models.BooleanField(default = True)

	def __unicode__(self):
		return str(self.user)

def create_person(sender, instance, created, **kwargs):  
  if created:  
    profile, created = Person.objects.get_or_create(user=instance)  

post_save.connect(create_person, sender=User) 

class Topic(models.Model):
	topic = models.CharField(max_length = 30, unique = True)
	details = models.CharField(max_length = 100, default = "")
	creator = models.ForeignKey(User, on_delete = models.CASCADE)
	create_date = models.DateTimeField(auto_now_add=True)
	is_verified = models.BooleanField(default = False)

	def __unicode__(self):
		return self.topic

	class Meta:
		ordering = ['topic']

class Question(models.Model):
	question = models.CharField(max_length = 30)
	details = models.CharField(max_length = 100, default = "")
	questioner = models.ForeignKey(User, on_delete = models.CASCADE)
	question_date = models.DateTimeField(auto_now_add=True)
	upvotes = models.IntegerField(blank = True, null = True)
	downvotes = models.IntegerField(blank = True, null = True)
	topic = models.ForeignKey(Topic, blank = True, null = True, on_delete = models.CASCADE)

	def __unicode__(self):
		return self.question

	class Meta:
		ordering = ['-question_date']

class Answer(models.Model):
	description = models.CharField(max_length = 100, default = "Description")
	question = models.ForeignKey(Question, on_delete = models.CASCADE)
	respondent = models.ForeignKey(User, on_delete = models.CASCADE)
	answer_date = models.DateTimeField(auto_now_add=True)
	upvotes = models.IntegerField(blank = True, null = True)
	downvotes = models.IntegerField(blank = True, null = True)

	def __unicode__(self):
		return self.answer

	class Meta:
		ordering = ['-answer_date']

class Instruction(models.Model):
	instruction = models.CharField(max_length = 100)
	answer = models.ForeignKey(Answer, on_delete = models.CASCADE)
	number = models.IntegerField(default = 1)
	image = models.FileField(upload_to=instruction_image_uploadpath, blank=True)

	def __unicode__(self):
		return self.instruction

	class Meta:
		ordering = ['number']

class Comment(models.Model):
	comment = models.CharField(max_length = 50)
	answer = models.ForeignKey(Answer, on_delete = models.CASCADE)
	commenter = models.ForeignKey(User, on_delete = models.CASCADE)
	comment_date = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.comment