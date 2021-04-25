from functools import wraps
from flask import g
import httpx


def requires_httpx_client(f):

    @wraps(f)
    async def wrapped(*args, **kwargs):
        g.client = httpx.AsyncClient()
        result = await f(*args, **kwargs)
        await g.client.aclose()
        return result

    return wrapped
