from django.contrib import admin

# Register your models here.
from timetable.models import Lesson, Subject

admin.site.register(Lesson)
admin.site.register(Subject)
