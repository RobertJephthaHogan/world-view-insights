import time
import numpy as np
from functools import wraps
from app.config import Settings
import asyncio

def timer(thing):
    @wraps(thing)
    async def wrapper():
        before = time.time()
        funct = await thing()
        print(f"The function : {thing.__name__} took {np.subtract(time.time(), before)} seconds")
        return funct
    return wrapper
