import requests
import pandas as pd
import datetime


def print_coin_or_coins(coin):
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


def get_historical_data(coin):
    url = 'https://coinmarketcap.com/currencies/{}/historical-data/?start=19760101&end=21000101'.format(coin)
    test_pandas = pd.read_html(url)
    df = test_pandas[0]
    return df


def average_opening_price(number_first_days, coin):
    df = get_historical_data(coin)
    return df.iloc[-number_first_days:, :]['Open'].mean()


def main():
    coin = 'ethereum'
    number_first_days = 3
    print(average_opening_price(number_first_days, coin))

if __name__ == '__main__':
    main()
