import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    #task1 = asyncio.create_task(
    #    say_after(3, 'hello'))

    #task2 = asyncio.create_task(
    #    say_after(5, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Ждём завершения обеих задач (это должно занять
    # около 2 секунд.)
    #await task1
    #await task2
    await say_after(3, 'hello')
    await say_after(5, 'world')

    print(f"finished at {time.strftime('%X')}")
asyncio.run(main())