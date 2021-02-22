import asyncio
import aiohttp
import yaml

payload = {
    'field': 'value',
}

headers = {
    'User-Agent': 'testing'
}

with open('def.yaml') as f:
    tests = yaml.safe_load(f).get('tests')
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



loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.gather(get(), post()))
loop.run_until_complete(run_tests())
