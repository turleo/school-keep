from django.contrib import admin

# Register your models here.
from timetable.models import Bell, Subject

admin.site.register(Bell)
admin.site.register(Subject)
