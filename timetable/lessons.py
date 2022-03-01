import time

from django.core.exceptions import ObjectDoesNotExist

import wsapi
from timetable.models import Lesson


@wsapi.add_callback("timetable.lessons.fetch")
def fetch(scope: dict, **kwargs):
    lessons = Lesson.objects.filter(owner=scope['user'])
    return {"event": "timetable.lessons", "data": list(map(lambda x: x.toJSON(), lessons))}


@wsapi.add_callback("timetable.lessons.change")
def change(scope: dict, **kwargs):
    lesson_data = kwargs.get("data")
    if lesson_data.get("id", 0) == 0:
        lesson = Lesson(subject_id=lesson_data.get("subject", {"id": 0})['id'],
                        bell_id=lesson_data.get("bell", {"id": 0})['id'],
                        day=lesson_data.get("day"),
                        owner=scope['user'])
    else:
        lesson = Lesson.objects.get(pk=lesson_data['id'])
        lesson.subject_id = lesson_data.get("subject", {"id": 0})['id']
        lesson.bell_id = lesson_data.get("bell", {"id": 0})['id']
        lesson.day = lesson_data['day']
        lesson.owner = scope['user']
    lesson.save()
    return wsapi.callbacks['timetable.lessons.fetch'](scope, **kwargs)


@wsapi.add_callback("timetable.lessons.delete")
def delete(scope: dict, **kwargs):
    try:
        lesson_id = kwargs.get("id", 0)
        lesson = Lesson.objects.get(pk=lesson_id)
        lesson.delete()
    except ObjectDoesNotExist:
        pass
    return wsapi.callbacks['timetable.lessons.fetch'](scope, **kwargs)
