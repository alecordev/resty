import json
import pathlib

import requests
import yaml

from .utils import generate_filename_path

HERE = pathlib.Path(__file__).parent

payload = {
    'field': 'value',
}

headers = {
    'User-Agent': 'testing'
}

with open(HERE.joinpath('definitions', 'resty.yaml')) as config:
    tests = yaml.safe_load(config).get('tests')
    print(tests)


def run_tests():
    for t in tests:
        res = None
        if t['action'] == 'post':
            res = requests.post(t['endpoint'], data=t['parameters'])
        elif t['action'] == 'get':
            res = requests.get(t['endpoint'], params=t['parameters'])
        if res is not None and t['save_response']:
            filename = generate_filename_path(location_path=HERE, config=t)
            with open(filename, mode='w') as f:
                f.write(json.dumps(res.json(), indent=4))


def main():
    run_tests()


if __name__ == '__main__':
    main()
