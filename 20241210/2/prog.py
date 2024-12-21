import asyncio
import random

async def merge(A, B, start, middle, finish, event_in1, event_in2, event_out):
    await event_in1.wait()
    if middle < finish:
        await event_in2.wait()
    i, j = start, middle
    b = start
    while i < middle and j < finish:
        if A[i] <= A[j]:
            B[b] = A[i]
            i += 1
        else:
            B[b] = A[j]
            j += 1
        b += 1

    while i < middle:
        B[b] = A[i]
        i += 1
        b += 1
    while j < finish:
        B[b] = A[j]
        j += 1
        b += 1
    event_out.set()

async def mtasks(A):
    AA = A[:]
    N = len(A)
    B = [0] * N
    tasks = []
    events = []
    for i in range(N):
        event = asyncio.Event()
        event.set()
        events.append(event)
    step = 1
    backwards = True
    while step < N:
        events_out = []
        for start in range(0, N, 2 * step):
            ev = asyncio.Event()
            events_out.append(ev)
            middle = min(start + step, N)
            if middle < N:
                ev2 = events[middle // step]
            else:
                ev2 = asyncio.Event()
            if backwards:
                tasks.append(merge(AA, B, start, middle, min(start + 2 * step, N), events[start // step], ev2, ev))
            else:
                tasks.append(merge(B, AA, start, middle, min(start + 2 * step, N), events[start // step], ev2, ev))
        backwards = not backwards
        events = events_out
        step *= 2

    return tasks, AA


import sys
exec(sys.stdin.read())
