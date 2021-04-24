from functools import wraps


def requires_auth(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        # TODO: Reject if unauthorized
        return f(*args, **kwargs)

    return wrapped
