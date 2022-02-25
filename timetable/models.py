import json

from django.contrib.auth.models import User
from django.db import models


class Bell(models.Model):
    start = models.TimeField()
    end = models.TimeField()
    days = models.CharField(max_length=20)  # coma separated two first symbols of days of the week
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def toJSON(self):
        out = {
            "id": str(self.id),
            "start": str(self.start),
            "end": str(self.end),
            "days": self.days.split(',')
        }
        return out

class Subject(models.Model):
    title = models.CharField(max_length=20)
    icon = models.CharField(max_length=1)  # emoji
    room = models.CharField(max_length=5)
    teacher = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def toJSON(self):
        out = {
            "id": str(self.id),
            "title": str(self.title),
            "icon": str(self.icon),
            "room": str(self.room),
            "teacher": str(self.teacher),
        }
        return out

