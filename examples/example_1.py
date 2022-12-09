import asyncio
import time

import async_executor


async def sleep_and_print(i):
    print(f'{i} {int(time.time())} - before sleep')
    await asyncio.sleep(1)
    print(f'{i} {int(time.time())} - after sleep')


async def main():
    # limit to a maximum of two concurrent executions
    executor = async_executor.AsyncExecutor(max_concurrent=2)

    # awaitables are only queued here - nothing is run
    for i in range(5):
        executor.submit(sleep_and_print, i)

    # awaitables begin executing
    async for task in executor:
        task.result()

asyncio.run(main())
