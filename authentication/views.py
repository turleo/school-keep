import uuid
from typing import Optional

from django.contrib.auth import authenticate
from .models import Token

import wsapi


@wsapi.add_callback("authentication.token")
def login_by_token(token: str, **kwargs) -> Token:
    saved = Token.objects.get(token=token)
    return saved


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
