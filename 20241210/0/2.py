import asyncio
import time

async def squarer(n):
    return n * n

async def doubler(n):
    return n * 2

async def main(x, y):
    print(x, y)
    x, y = await asyncio.gather(squarer(x), squarer(y))
    x, y = await asyncio.gather(doubler(x), doubler(y))
    print(x, y)

asyncio.run(main(2, 3))
