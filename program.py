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


def average_opening_price(number_days, df):
    df = df[df.loc[:, 'Market Cap'] != '-']  # Remove Null Market Caps
    return df.iloc[-number_days:, :]['Open'].mean()


def opening_price(number_days, df):
    df = df[df.loc[:, 'Market Cap'] != '-']  # Remove Null Market Caps
    return df.iloc[-number_days, :]['Open'].mean()


def print_alive_prices(coin, days_alive, number_days, df):
    print('{} has been alive for {} days.'.format(coin, days_alive))
    print('First {} days average opening price: '.format(number_days) +
          '{}'.format(average_opening_price(number_days, df)))
    for i in range(30, days_alive, 30):
        print('Price at {} days: {}'.format(i, opening_price(i, df)))


def main():
    coin = 'ethereum'
    df = get_historical_data(coin)
    days_alive = df.shape[0]
    number_days = 3
    print_alive_prices(coin, days_alive, number_days, df)

if __name__ == '__main__':
    main()
