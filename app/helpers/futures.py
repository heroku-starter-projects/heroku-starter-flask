import asyncio


def synchronize(promise):
    try:
        loop = asyncio.get_event_loop()
    except Exception:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    result = loop.run_until_complete(promise)
    loop.close()

    return result


# Equivalent to
# Promise.all(args.map((...arg) => fun(...arg)))
def list_map(fun, *args):
    promises = list(map(fun, *args))
    return asyncio.gather(*promises)


async def serial_await(fun, cb=lambda x: x, *args):
    result = []
    for arg_tuple in zip(*args):
        cb(arg_tuple)
        result.append(await fun(*arg_tuple))

    return result


# https://stackoverflow.com/a/312464/1217998
def chunkify(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


async def batched_serial(batch_size, fun, cb=lambda x: x, *args):
    zipped_args = list(zip(*args))
    chunks = chunkify(zipped_args, batch_size)
    result = []

    for chunk in chunks:
        # https://stackoverflow.com/a/19343/1217998
        chunk = zip(*chunk)
        intermediate = await list_map(fun, *chunk)
        cb(intermediate)

        result += intermediate

    return result


# https://stackoverflow.com/a/46324983/1217998
def async_test(coro):
    def wrapper(*args, **kwargs):
        loop = asyncio.new_event_loop()
        return loop.run_until_complete(coro(*args, **kwargs))
    return wrapper


# https://stackoverflow.com/a/61472246/1217998
async def resolve(val):
    return val


async def throttled_gather(limit, tasks):
    semaphore = asyncio.Semaphore(limit)

    async def sem_task(task):
        async with semaphore:
            return await task
    return await asyncio.gather(*(sem_task(task) for task in tasks))
