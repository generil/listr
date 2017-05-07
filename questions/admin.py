from django.contrib import admin
# from models import User
from .models import Topic
from .models import Question
from .models import Answer
from .models import Comment

admin.site.register(Topic)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Comment)
