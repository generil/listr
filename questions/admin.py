from django.contrib import admin
# from models import User
from .models import Person
from .models import Topic
from .models import Question
from .models import Answer
from .models import Instruction
from .models import Comment

admin.site.register(Person)
admin.site.register(Topic)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Instruction)
admin.site.register(Comment)
