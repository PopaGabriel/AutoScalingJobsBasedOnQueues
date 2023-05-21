import aiohttp
import asyncio
import requests


async def test_endurance_asyncio():
    for _ in range(1000):
        async with aiohttp.ClientSession() as session:
            async with session.post(
                "http://127.0.0.1:5000/example1/wait_celery/2"
            ) as resp:
                print(await resp.text())


def test_endurance_normal():
    for _ in range(10):
        print(requests.post("http://127.0.0.1:5000/example1/wait/2"))


if __name__ == "__main__":
    # asyncio.run(test_endurance_asyncio())
    test_endurance_normal()
