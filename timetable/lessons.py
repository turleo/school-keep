import time

import wsapi
from timetable.models import Lesson


@wsapi.add_callback("timetable.lessons.fetch")
def fetch(scope: dict, **kwargs) -> list:
    lessons = Lesson.objects.filter(owner=scope['user'])
    return list(map(lambda x: x.toJSON(), lessons))


@wsapi.add_callback("timetable.lessons.add")
def add(scope: dict, **kwargs) -> list:
    start = kwargs.get("start")
    end = kwargs.get("end")
    days = kwargs.get("days")

    lesson = Lesson(
        start=start,
        end=end,
        days=days,
        owner=scope['user']
    )
    lesson.save()
    return wsapi.callbacks['timetable.lessons.fetch'](scope, **kwargs)
