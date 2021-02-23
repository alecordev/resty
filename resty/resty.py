import pathlib
import asyncio
import datetime

import aiohttp
import aiofiles
import yaml

HERE = pathlib.Path(__file__).parent

payload = {
    'field': 'value',
}

headers = {
    'User-Agent': 'testing'
}

with open('def.yaml') as config:
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
    async with aiohttp.ClientSession(headers=headers) as session:
        for t in tests:
            if t['action'] == 'post':
                async with session.post(t['endpoint'], json=t['parameters']) as resp:
                    res = await resp.text()
                    # print(resp)
                    print(res)
                    if t['save_response']:
                        timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%d_%H%M%S')
                        path = HERE.joinpath(t['save_dir'])
                        path.mkdir(exist_ok=True)
                        filename = f"{t['save_prefix']}_{t['name'].lower().replace(' ', '_')}_{timestamp}.{t['save_extension'].lower()}"
                        async with aiofiles.open(path.joinpath(filename), mode='w') as f:
                            await f.write(res)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(asyncio.gather(get(), post()))
    loop.run_until_complete(run_tests())
