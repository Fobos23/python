from functools import wraps

from core import log


def autolog(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            log.info(f'Execute function: {func.__name__}')
            return func(*args, **kwargs)
        except Exception as e:
            log.error(f'Function: {func.__name__} failed - {e}')
    return wrapper