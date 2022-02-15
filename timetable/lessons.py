import wsapi
from timetable.models import Lesson


@wsapi.add_callback("timetable.lessons.add")
def add(scope: dict, **kwargs) -> dict:
    pass


@wsapi.add_callback("timetable.lessons.fetch")
def fetch(scope: dict, **kwargs) -> list:
    lessons = Lesson.objects.filter(owner=scope['user'])
    return list(map(lambda x: x.toJSON(), lessons))
