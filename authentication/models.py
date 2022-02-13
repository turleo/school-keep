from django.contrib.auth.models import User
from django.db import models


class Token(models.Model):
    token = models.CharField(max_length=32)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_ip = models.GenericIPAddressField()
    user_agent = models.CharField(max_length=200)
    last_online = models.DateTimeField(auto_now=True)

