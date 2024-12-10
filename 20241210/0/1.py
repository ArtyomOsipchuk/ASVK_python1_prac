import asyncio
import time

async def late(sec):
    s = time.strftime("%X")
    await asyncio.sleep(sec)
    return sec, s, time.strftime("%X")

async def main():
    print(*await late(1))
    print(*await late(2))
    print(*await asyncio.gather(late(3), late(4), late(5)))
    task6 = asyncio.create_task(late(6))
    task7 = asyncio.create_task(late(7))
    print(*await task6)
    print(*await task7)
    


asyncio.run(main())
