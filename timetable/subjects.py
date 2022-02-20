from django.core.exceptions import ObjectDoesNotExist

import wsapi
from timetable.models import Subject


@wsapi.add_callback("timetable.subjects.fetch")
def fetch(scope: dict, **kwargs) -> list:
    subjects = Subject.objects.filter(owner=scope['user'])
    return list(map(lambda x: x.toJSON(), subjects))


@wsapi.add_callback("timetable.subjects.add")
def add(scope: dict, **kwargs) -> list:
    title = kwargs.get("title")
    icon = kwargs.get("icon", "")
    room = kwargs.get("room", "")
    teacher = kwargs.get("teacher", "")

    subject = Subject(
        title=title,
        icon=icon,
        room=room,
        teacher=teacher,
        owner=scope['user']
    )
    subject.save()
    return wsapi.callbacks['timetable.subjects.fetch'](scope, **kwargs)


@wsapi.add_callback("timetable.subjects.change")
def change(scope: dict, **kwargs):
    data = kwargs.get("data")
    if data.get("id", 0) == 0:
        title = data.get("title")
        icon = data.get("icon", "")
        room = data.get("room", "")
        teacher = data.get("teacher", "")

        subject = Subject(
            title=title,
            icon=icon,
            room=room,
            teacher=teacher,
            owner=scope['user']
        )
        subject.save()
    else:
        subject = Subject.objects.get(pk=data['id'])
        subject.title = data.get("title")
        subject.icon = data.get("icon", "")
        subject.room = data.get("room", "")
        subject.teacher = data.get("teacher", "")
    subject.save()
    return wsapi.callbacks['timetable.subjects.fetch'](scope, **kwargs)


@wsapi.add_callback("timetable.subjects.delete")
def delete(scope: dict, **kwargs):
    try:
        subject_id = kwargs.get("id", 0)
        subject = Subject.objects.get(pk=subject_id)
        subject.delete()
    except ObjectDoesNotExist:
        pass
    return wsapi.callbacks['timetable.subjects.fetch'](scope, **kwargs)
