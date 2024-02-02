import time
import numpy as np
from functools import wraps
import asyncio

def throttle(func):
    @wraps(func)
    async def wrapper(self):
        throttle_start_time = False
        try:
            funct = await func(self)
        except Exception as ex:
            throttle_start_time = time.time()
            print(ex)
            if '429' in str(ex):
                print("Too many requests: 429 API limit exceeded. Engaging throttle...")
            x = 0.1
            time.sleep(x)
            successful = False

            while not successful:
                try:
                    funct = await func(self)
                    successful = True
                except Exception as ex:
                    x = np.multiply(x, 2)
                    time.sleep(x)
                    print("   \u27B5 throttling requests...")
                    pass
                    funct = None
            else:
                print('something went wrong here')   
        if throttle_start_time:
            print(f"   \u27B5 \u27B5 \u27B5  Throttling for : {func.__name__} took {np.subtract(time.time(), throttle_start_time)} seconds")
        return funct
    return wrapper



