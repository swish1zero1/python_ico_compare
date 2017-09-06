import json
from pprint import pprint
import requests


def main():
    coin = 'ethereum'

    r = requests.get('https://api.coinmarketcap.com/v1/ticker/')

    if coin is not '':
        print('Searching coin {}'.format(coin))
        for line in r.json():
            if line['id'] == coin:
                print(line)
                break  # Once found, stop the loop
    else:
        print('Coin field is blank. Printing all coins:')
        for line in r.json():
            print(line)


if __name__ == '__main__':
    main()
