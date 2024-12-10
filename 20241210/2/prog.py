import asyncio
import random

async def merge(A, B, start, middle, finish, event_in1, event_in2, event_out):
    await event_in1.wait()
    await event_in2.wait()
    B[start:finish] = A[start:middle] + A[middle:finish]
    event_out.set()

async def mtasks(A):
    N = len(A)
    B = [0] * N
    tasks = []
    events_in1 = [asyncio.Event() for i in range(N)]
    events_in2 = [asyncio.Event() for i in range(N)]
    events_out = [asyncio.Event() for i in range(N)]
    for i in range(N):
        tasks.append(merge(A, B, i, i + 1, min(i + 2, N), events_in1[i], events_in2[i], events_out[i]))
        await events_out[i].wait()
    
    for length in range(1, N, length * 2):
        for i in range(0, N, length * 2):
            mid = min(i + length, N)
            end = min(i + length * 2, N)
            tasks.append(merge(A, B, i, mid, end, events_in1[length // 2], events_in2[length // 2], events_out[length // 2]))
            await events_out[length // 2].wait()
        A[:N] = B[:N]

    return tasks, B

import asyncio

async def main(A):
    tasks, B = await mtasks(A)
    print(len(tasks))
    random.shuffle(tasks)
    await asyncio.gather(*tasks)
    return B

random.seed(1337)
A = random.choices(range(10), k=33)
B = asyncio.run(main(A))
print(*A)
print(*B)
print(B == sorted(A))
