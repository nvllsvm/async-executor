# async-executor
[![PyPI - Version](https://img.shields.io/pypi/v/async-executor.svg)](https://pypi.org/project/async-executor)

Async execution pool

## Examples
### Limit the number of concurrently running awaitables
```python
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
```

This shows that only a maximum of two executions are allowed to run concurrently.
```
$ python examples/example_1.py
0 1670613515 - before sleep
1 1670613515 - before sleep
0 1670613516 - after sleep
1 1670613516 - after sleep
2 1670613516 - before sleep
3 1670613516 - before sleep
2 1670613517 - after sleep
3 1670613517 - after sleep
4 1670613517 - before sleep
4 1670613518 - after sleep
```

## Installation

```console
pip install async-executor
```

## License

`async-executor` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
