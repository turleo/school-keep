import wsapi
from hometask.models import Hometask, Task


@wsapi.add_callback("hometask.fetch")
def get_hometasks(scope: dict, **kwargs):
    hometasks = Hometask.objects.filter(owner=scope['user'])
    return {"event": "hometask", "data": list(map(lambda x: x.toJSON(), hometasks))}


@wsapi.add_callback("hometask.change")
def change_hometasks(scope: dict, **kwargs):
    kwargs = kwargs['data']
    hometask_id = kwargs.get("id", 0)
    if hometask_id != 0:
        hometasks = Hometask.objects.get(pk=hometask_id)
        hometasks.subject_id = kwargs["subject"]
        hometasks.deadline = kwargs["deadline"]
        hometasks.save()
    else:
        Hometask(
            subject_id=kwargs["subject"],
            deadline=kwargs["deadline"],
            owner=scope['user']
        ).save()
    return wsapi.callbacks['hometask.fetch'](scope, **kwargs)


@wsapi.add_callback("hometask.task.change")
def change_hometasks(scope: dict, **kwargs):
    kwargs = kwargs['data']
    task_id = kwargs.get("id", 0)
    if task_id != 0:
        task = Task.objects.get(pk=task_id)
        task.text = kwargs["text"]
        task.done = kwargs["done"]
        task.save()
    else:
        Task(
            hometask_id=kwargs["homework_id"],
            text=kwargs["text"],
            done=False
        ).save()
    return wsapi.callbacks['hometask.fetch'](scope, **kwargs)
