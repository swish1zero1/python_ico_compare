import requests
import pandas as pd
import datetime


# def print_coin_or_coins(coin):
#     r = requests.get('https://api.coinmarketcap.com/v1/ticker/')
#
#     if coin is not '':
#         print('Searching coin {}'.format(coin))
#         for line in r.json():
#             if line['id'] == coin:
#                 print(line)
#                 break  # Once found, stop the loop
#     else:
#         print('Coin field is blank. Printing all coins:')
#         for line in r.json():
#             print(line)


def get_historical_data(coin):
    """
    • Takes specified coin and grabs the historical data from Coinmarketcap.com
    • Checks if the URL redirected to /assets/ instead of /currencies/ meaning the coin is a token and adjusts
    the URL accordingly
    :param coin: coin input to add to URL
    :return: first items in list (read_html returns a list of data frames)
    """

    url = 'https://coinmarketcap.com/currencies/{}/historical-data/?start=20000428&end=21000906'.format(coin)
    test_pandas = pd.read_html(url)
    if test_pandas[0].shape[0] < 40:  # check if coin is 'asset' and url redirected
        url = 'https://coinmarketcap.com/assets/{}/historical-data/?start=19760101&end=21000101'.format(coin)
        test_pandas = pd.read_html(url)
    df = test_pandas[0]
    return df


def average_opening_price(number_days, df):
    """
    • Checks if dataframe has Null Market Caps and removes them
    :param number_days: The number of days after the coin hits the exchanges (Averaged)
    :param df: data frame gathered from CoinMarketCap
    :return: the specified number of days' average opening price
    """
    if df.iloc[-1, :]['Market Cap'] == '-':  # If Data frame has Null Market Caps
        df = df[df.loc[:, 'Market Cap'] != '-']  # Remove Null Market Caps
    return df.iloc[-number_days:, :]['Open'].mean()


def opening_price(number_days, df):
    """
    :return: the opening price of specified numbers of days
    """
    return df.iloc[-number_days, :]['Open']


def print_alive_prices(coin, days_alive, number_days, df):
    """

    :param coin:
    :param days_alive: days the coin has been running (after the start date)
    :param number_days: number of days averaged in the beginning (defines the start date)
    :param df: data frame gathered from CoinMarketCap
    :return:
    """
    interval_list = []
    aop = average_opening_price(number_days, df)
    print('{} has been alive for {} days.'.format(coin, days_alive))
    print('First {} days average opening price: '.format(number_days) +
          '{}'.format(aop))
    for i in range(1, days_alive - 1):
        # print('Price at {} days: {}'.format(i, opening_price(i, df)))
        interval_list.append(opening_price(i, df))
    return aop, interval_list


def check_price_decrease(aop_list_tuple):
    """
    • Compares the Average Opening Price to the subsequent days
    :param aop_list_tuple: a tuple that contains the Average Opening Price averaged with sepcified set of days and
    a list of all of the subsequent days and their opening prices
    :return: nothing only prints
    """
    temp_int = 0
    start_date = 30
    for i in range(start_date, len(aop_list_tuple[1])):
        if aop_list_tuple[0] < aop_list_tuple[1][i]:
            print('Day {}: {} the price was higher than ICO: {}'.format(i, aop_list_tuple[1][i], aop_list_tuple[0]))
            temp_int = i
            break
    for i in range(temp_int, len(aop_list_tuple[1])):
        if (2 * aop_list_tuple[0]) < aop_list_tuple[1][i]:
            print('Day {}: {} the price was more than double the ICO'.format(i, aop_list_tuple[1][i]))
            temp_int = i
            break
    for i in range(temp_int, len(aop_list_tuple[1])):
        if (3 * aop_list_tuple[0]) < aop_list_tuple[1][i]:
            print('Day {}: {} the price was more than triple the ICO'.format(i, aop_list_tuple[1][i]))
            temp_int = i
            break
    for i in range(temp_int, len(aop_list_tuple[1])):
        if (10 * aop_list_tuple[0]) < aop_list_tuple[1][i]:
            print('Day {}: {} the price was more than ten times the ICO'.format(i, aop_list_tuple[1][i]))
            temp_int = i
            break


def main():
    """
    • Specify coin
    • Create Data Frame
    • days_alive = length of the Data Frame
    • number_days = changeable number of days to average in the beginning of the coin hitting the exchanges
    • Created tuple with all days opening prices and prints days alive and average opening price given the beginning
    number of days
    • Compares the average opening price with subsequent days
    :return: nothing
    """
    coin = 'bitshares'
    df = get_historical_data(coin)
    days_alive = df.shape[0]
    number_days = 10
    # aop = Average Opening Price
    aop_list_tuple = print_alive_prices(coin, days_alive, number_days, df)
    check_price_decrease(aop_list_tuple)


if __name__ == '__main__':
    main()
