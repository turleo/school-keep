import time

from django.core.exceptions import ObjectDoesNotExist

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


@wsapi.add_callback("timetable.lessons.change")
def change(scope: dict, **kwargs):
    bell_data = kwargs.get("data")
    if bell_data.get("id", 0) == 0:
        bell = Lesson(start=bell_data['start'], end=bell_data['end'], days=",".join(bell_data['days']), owner=scope['user'])
    else:
        bell = Lesson.objects.get(pk=bell_data['id'])
        bell.start = bell_data['start']
        bell.end = bell_data['end']
        bell.days = ",".join(bell_data['days'])
    bell.save()
    return wsapi.callbacks['timetable.lessons.fetch'](scope, **kwargs)


@wsapi.add_callback("timetable.lessons.delete")
def delete(scope: dict, **kwargs):
    try:
        bell_id = kwargs.get("id", 0)
        bell = Lesson.objects.get(pk=bell_id)
        bell.delete()
    except ObjectDoesNotExist:
        pass
    return wsapi.callbacks['timetable.lessons.fetch'](scope, **kwargs)
