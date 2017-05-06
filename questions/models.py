from django.db import models

class User(models.Model):
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	username = models.CharField(max_length = 15, unique = True)
	password = models.CharField(max_length = 30)
	email = models.CharField(max_length = 30, unique = True)
	institution = models.CharField(max_length = 30)
	position = models.CharField(max_length = 30)
	join_date = models.DateField()
	is_verified = models.BooleanField(default = True)

	def __str__(self):
		return self.first_name + ' ' + self.last_name

class Topic(models.Model):
	topic = models.CharField(max_length = 30, unique = True)
	details = models.CharField(max_length = 100)
	user_id = models.ForeignKey(User, on_delete = models.CASCADE)
	create_date = models.DateField()

	def __str__(self):
		return self.topic

class Question(models.Model):
	question = models.CharField(max_length = 30)
	details = models.CharField(max_length = 100)
	user_id = models.ForeignKey(User, on_delete = models.CASCADE)
	question_date = models.DateField()
	upvotes = models.IntegerField()
	downvotes = models.IntegerField()
	topic = models.ForeignKey(Topic, blank = True, null = True, on_delete = models.CASCADE)

	def __str__(self):
		return self.question

class Answer(models.Model):
	answer = models.CharField(max_length = 500)
	question = models.ForeignKey(Question, on_delete = models.CASCADE)
	user_id = models.ForeignKey(User, on_delete = models.CASCADE)
	answer_date = models.DateField()
	upvotes = models.IntegerField()
	downvotes = models.IntegerField()

	def __str__(self):
		return self.answer

class Comment(models.Model):
	comment = models.CharField(max_length = 50)
	answer = models.ForeignKey(Answer, on_delete = models.CASCADE)
	user_id = models.ForeignKey(User, on_delete = models.CASCADE)
	comment_date = models.DateField()

	def __str__(self):
		return self.comment