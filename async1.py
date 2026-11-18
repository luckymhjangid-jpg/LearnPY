import asyncio

async def para2():
    print("This is me")
    await asyncio.sleep(1)
    print("writing the code and learning about asyncio")
    await asyncio.sleep(2)
    print('now this will run after two seconds')

asyncio.run(para2())