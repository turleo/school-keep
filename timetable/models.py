import json

from django.contrib.auth.models import User
from django.db import models


class Lesson(models.Model):
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

