from .consumer import callbacks


def add_callback(event: str):
    def decorator(func):
        callbacks[event] = func
    return decorator
