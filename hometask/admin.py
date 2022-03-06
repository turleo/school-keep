from django.contrib import admin

# Register your models here.
from hometask.models import Hometask, Task

admin.site.register(Hometask)
admin.site.register(Task)
