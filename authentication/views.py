import uuid
from typing import Optional, Dict

from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist

from .models import Token

import wsapi


@wsapi.add_callback("authentication.token")
def login_by_token(scope: dict, **kwargs):
    try:
        saved = Token.objects.get(token=kwargs.get("token", ""))
        return saved
    except ObjectDoesNotExist:
        return None


@wsapi.add_callback("authentication.user")
def login_by_password(scope: dict, **kwargs) -> Optional[Token]:
    user = authenticate(username=kwargs.get("username", ""),
                        password=kwargs.get("password", ""))
    if user is None:
        return None
    useragent = "bot"
    for i in scope['headers']:
        if i[0] == b'user-agent':
            useragent = i[0].decode
    saved = Token(
        user=user,
        last_ip=scope['client'][0],
        user_agent=useragent,
        token=uuid.uuid4().hex
    )
    saved.save()
    return saved
