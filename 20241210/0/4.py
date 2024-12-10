import asyncio


async def snd(event):
    event.set()
    print(f'SND: evsnd sended...')

async def mid(k, evcnd, event):
    await evcnd.wait()
    event.set()
    print(f'MID{k}: evmid{k} sended...')

async def rcv(evmid0, evmid1):
    await evmid0.wait()
    print(f'RCV: …evmid0 got it!')
    await evmid1.wait()
    print(f'RCV: …evmid1 got it!')


async def main():
    evmid0 = asyncio.Event() 
    evmid1 = asyncio.Event() 
    evcnd = asyncio.Event() 
    await asyncio.gather(
        rcv(evmid0, evmid1),
        mid(1, evcnd, evmid1),
        mid(0, evcnd, evmid0),
        snd(evcnd)
    )

asyncio.run(main())
