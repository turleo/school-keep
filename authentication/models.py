from django.contrib.auth.models import User
from django.db import models


class Token(models.Model):
    token = models.CharField(max_length=32)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_ip = models.GenericIPAddressField()
    user_agent = models.CharField(max_length=200)
    last_online = models.DateTimeField(auto_now=True)

    def toJSON(self):
        out = {
            "id": str(self.id),
            "last_ip": str(self.last_ip),
            "useragent": str(self.user_agent),
            "last_online": str(self.last_online)
        }
        return out

