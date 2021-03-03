import pathlib
import asyncio

import aiohttp
import aiofiles
import yaml

from .utils import generate_filename_path

HERE = pathlib.Path(__file__).parent

payload = {
    'field': 'value',
}

headers = {
    'User-Agent': 'testing'
}

with open(HERE.joinpath('definitions', 'aioresty.yaml')) as config:
    tests = yaml.safe_load(config).get('tests')
    print(tests)


async def get():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://httpbin.org/get') as resp:
            print(resp.status)
            print(await resp.text())


async def post():
    async with aiohttp.ClientSession() as session:
        async with session.post('http://httpbin.org/post', json=payload) as resp:
            print(resp.status)
            print(await resp.text())


async def run_tests():
    res = None
    async with aiohttp.ClientSession(headers=headers) as session:
        for t in tests:
            if t['action'] == 'post':
                async with session.post(t['endpoint'], json=t['parameters']) as resp:
                    res = await resp.text()
                    print(res)
            elif t['action'] == 'get':
                async with session.get(t['endpoint'], params=t['parameters']) as resp:
                    res = await resp.text()
                    print(res)
            if t['save_response'] and (res is not None):
                filename = generate_filename_path(location_path=HERE, config=t)
                async with aiofiles.open(filename, mode='w') as f:
                    await f.write(res)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(asyncio.gather(get(), post()))
    loop.run_until_complete(run_tests())
