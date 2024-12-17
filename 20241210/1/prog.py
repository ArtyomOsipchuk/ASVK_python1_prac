import asyncio

async def writer(queue, delay):
    i = 0
    while True:
        await asyncio.sleep(delay)
        val = f"{i}_{delay}"
        await queue.put(val)
        i += 1

async def stacker(queue, stack):
    while True:
        val = await queue.get()
        await stack.put(val)

async def reader(stack, n, delay):
    while n:
        await asyncio.sleep(delay)
        print(await stack.get())
        n -= 1

async def main():
    d1, d2, d3, n = eval(input())
    queue = asyncio.Queue()
    stack = asyncio.Queue()

    task1 = asyncio.create_task(reader(stack, n, d3))
    task2 = asyncio.create_task(writer(queue, d1))
    task3 = asyncio.create_task(writer(queue, d2))
    task4 = asyncio.create_task(stacker(queue, stack))
    await task1
    task2.cancel()
    task3.cancel()
    task4.cancel()

#asyncio.run(main())
