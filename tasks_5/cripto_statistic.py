#!/usr/bin/python3

import requests
import json
import time


def fetch_criptostatistic():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': '20',
        'page': '1',
        'sparkline': 'false',
        'price_change_percentage': '24h',
        'market_data': 'true'
    }
    respons = requests.get(url, params=params)
    data = respons.json()
    return data


def display_stats(data):
    print(data)
    for crypto in data:
        name = crypto['name']
        symbol = crypto['symbol'].upper()
        price = crypto['current_price']
        market_cap = crypto['market_cap']
        total_volume = crypto['total_volume']
        price_change_24h = crypto['price_change_24h']

    print("Name\tSymbol\tPrice(USD)\tMarket Cap\tTotal Volume\tChange (24h)")
    print(f"{name}\t{symbol}\t{price}\t{market_cap}\t{total_volume}\t{price_change_24h}")

    print("=" * 80)



def filter_by_name(data, keyword):
    filtered_data = [crypto for crypto in data if keyword.lower() in crypto['name'].lower()  ]
    return filtered_data

#
def filter_by_value(data, value):
    filtered_data = [crypto for crypto in data if crypto['current_price'] > value]
    return filtered_data

def main():

    while True:
        try:
            keyword = input("Filter by name (leave blank for no filter): ")
            value = float(input("Filter by value (leave blank for no filter): ") or 0)
            stats = fetch_criptostatistic()
            display_stats(stats)
            print("=" * 80)

            if keyword:
                stats = filter_by_name(stats, keyword)
            if value:
                stats = filter_by_value(stats, value)

            display_stats(stats)
        except ValueError:
            print("Invalid input for filter value. Please enter a valid number.")
        except Exception as e:
            print("An error occurred:", e)

        time.sleep(5)

if __name__ == "__main__":
    main()

