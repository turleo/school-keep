from django.contrib.auth.models import User
from django.db import models

from timetable.models import Subject


class Hometask(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    deadline = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def toJSON(self):
        tasks = Task.objects.filter(hometask=self)
        tasks_json = map(lambda x: x.toJSON(), tasks)
        return {
            "id": self.id,
            "subject": self.subject.toJSON(),
            "deadline": str(self.deadline),
            "tasks": list(tasks_json)
        }


class Task(models.Model):
    text = models.TextField()
    done = models.BooleanField()
    hometask = models.ForeignKey(Hometask, on_delete=models.CASCADE)

    def toJSON(self):
        return {
            "text": self.text,
            "done": self.done,
            "id": self.id
        }
