import asyncio

async def square(n, delay):
    print(f"started {n}(will take {delay}s)")
    await asyncio.sleep(delay)
    print(f"Finished{n}")
    return n * n

async def main():
    result = await asyncio.gather(
        square(2,4),
        square(3,2),
        square(4,1)
    )
    print("final list",result)

asyncio.run(main())