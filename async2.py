# import time 
# def task(name):
#     print("f{name} started")
#     time.sleep(3)
#     print("f{name} ended")

# task("task1")

import asyncio
async def task(name):
    print(f"{name} started")
    await asyncio.sleep(3)
    print(f"{name} ended")


async def main():
    await asyncio.gather(
        task("task1"),
        task("task2"),
        task("task3")
    )
asyncio.run(main())
