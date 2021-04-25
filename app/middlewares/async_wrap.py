from functools import wraps
from app.helpers.futures import synchronize


# https://stackoverflow.com/a/55546746/1217998
def async_wrap(f):

    @wraps(f)
    def wrapped(*args, **kwargs):
        return synchronize(f(*args, **kwargs))

    return wrapped
