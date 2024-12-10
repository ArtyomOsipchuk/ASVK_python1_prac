import asyncio

async def main():
    queue1 = asyncio.Queue()
    queue2 = asyncio.Queue()
    # реализация балдежа
    #await asyncio.gather(
    #    prod(queue1),
    #    mid(queue1, queue2),
    #    cons(queue2)
    #)
    task1 = asyncio.create_task(prod(queue1))
    task2 = asyncio.create_task(mid(queue1, queue2))
    task3 = asyncio.create_task(cons(queue2))
    await task1
    task2.cancel()
    task3.cancel()
    print("ALL DONE")

async def prod(queue):
    for i in range(5):
        val = f"PROD: value_{i}"
        await queue.put(val)
        print(f"PROD: Put <{val}> to q1")
        await asyncio.sleep(1)

async def mid(queue1, queue2):
    while True:
        res = await queue1.get()
        print(f"\tMID: Got {res} from q1")
        await queue2.put(res)
        print(f"\tMID: Put <{res}> to q2")

async def cons(queue):
    while True:
        res = await queue.get()
        print(f"\t\tCONS: Got {res} from q2")

asyncio.run(main())

