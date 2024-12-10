import asyncio

async def late(delay, msg):
    await asyncio.sleep(delay)
    print(msg)
    return delay

async def main():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(late(3, "A"))
        tg.create_task(late(1, "B"))
        tg.create_task(late(2, "C"))
    print("Done")

asyncio.run(main())
