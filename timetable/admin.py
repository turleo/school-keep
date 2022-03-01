from django.contrib import admin

# Register your models here.
from timetable.models import Bell, Subject, Lesson

admin.site.register(Bell)
admin.site.register(Lesson)
admin.site.register(Subject)
