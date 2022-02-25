import time

from django.core.exceptions import ObjectDoesNotExist

import wsapi
from timetable.models import Bell


@wsapi.add_callback("timetable.bells.fetch")
def fetch(scope: dict, **kwargs) -> list:
    lessons = Bell.objects.filter(owner=scope['user'])
    return list(map(lambda x: x.toJSON(), lessons))


@wsapi.add_callback("timetable.bells.change")
def change(scope: dict, **kwargs):
    bell_data = kwargs.get("data")
    if bell_data.get("id", 0) == 0:
        bell = Bell(start=bell_data['start'], end=bell_data['end'], days=",".join(bell_data['days']), owner=scope['user'])
    else:
        bell = Bell.objects.get(pk=bell_data['id'])
        bell.start = bell_data['start']
        bell.end = bell_data['end']
        bell.days = ",".join(bell_data['days'])
    bell.save()
    return wsapi.callbacks['timetable.bells.fetch'](scope, **kwargs)


@wsapi.add_callback("timetable.bells.delete")
def delete(scope: dict, **kwargs):
    try:
        bell_id = kwargs.get("id", 0)
        bell = Bell.objects.get(pk=bell_id)
        bell.delete()
    except ObjectDoesNotExist:
        pass
    return wsapi.callbacks['timetable.bells.fetch'](scope, **kwargs)
