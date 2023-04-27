import asyncio

async def async_sleep(n):
    print("before sleep", n)
    for i in range(n):
        await asyncio.sleep(i+1)
        print(f"slept for {i+1} seconds for n={n}")
    print("after sleep", n)

async def print_hello():
    print("hello")

async def main():
    # task = asyncio.create_task(async_sleep(4))
    # if a certain task is taking too long to execute, we can set a timeout to avoid clogging
    try:
        results = await asyncio.gather(
            asyncio.wait_for(async_sleep(10), 5),
            async_sleep(3),
            print_hello()
        )
    except asyncio.TimeoutError:
        print("Encountered timeout")
    else:
        print(results)

asyncio.run(main())