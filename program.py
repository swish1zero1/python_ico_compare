import json
from pprint import pprint
import requests


def main():
    r = requests.get('https://api.coinmarketcap.com/v1/ticker/')
    for line in r.json():
        print(line['id'])


if __name__ == '__main__':
    main()
