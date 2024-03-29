import uuid
from typing import Optional, Dict, List

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
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
    user = authenticate(username=kwargs.get("username", "").replace("@", ""),
                        password=kwargs.get("password", ""))
    if user is None:
        return None
    useragent = "bot"
    for i in scope['headers']:
        if i[0] == b'user-agent':
            useragent = i[1].decode()
    saved = Token(
        user=user,
        last_ip=scope['client'][0],
        user_agent=useragent,
        token=uuid.uuid4().hex
    )
    saved.save()
    return saved


@wsapi.add_callback("authentication.register")
def register(scope: dict, **kwargs) -> Optional[Token]:
    email = kwargs.get("username")
    password = kwargs.get("password")
    if not email or not password:
        return None
    username = email.replace("@", "")
    User.objects.create_user(username, email, password)

    return wsapi.callbacks["authentication.user"](scope, **kwargs)


@wsapi.add_callback("authentication_info.devices")
def register(scope: dict, **kwargs) -> List[Token]:
    tokens = Token.objects.filter(user=scope['user'])
    return list(map(Token.toJSON, tokens))


@wsapi.add_callback("authentication_info.kick")
def register(scope: dict, **kwargs) -> bool:
    kwargs.get("id", 0)
    token = Token.objects.get(pk=id)
    if token.user is scope['user']:
        token.delete()
    return wsapi.callbacks["authentication_info.devices"](scope, **kwargs)

