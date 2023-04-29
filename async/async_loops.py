import time
import asyncio

async def sleep(n):
    for i in range(1, n+1):
        yield i
        await asyncio.sleep(i)
        print(f"Slept for {i} seconds")

async def main():
    start = time.time()

    # it will take same time as synchronous for loop, it's just that we can transfer control
    # to other tasks if it is taking time 
    async for i in sleep(10):
        print(i)

    end = time.time()
    print(f"Took {end-start} seconds")

asyncio.run(main())