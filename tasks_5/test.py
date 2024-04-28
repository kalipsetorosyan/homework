import requests
import time
#!/usr/bin/python3


def fetch_crypto_stats():
    try:
        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {
            "vs_currency": "usd",
            "order": "market_cap_desc",
            "per_page": 20,
            "page": 1,
            "sparkline": False,
            "price_change_percentage": "24",
            'market_data': 'true'
        }

        response = requests.get(url, params=params)
        data = response.json()
        # print(data)
        return data
    except Exception as e:
        print("An error occurred while fetching crypto stats:", e)
        return []


def display_stats(data):
    try:
        print("=" * 10 + 'obout cripto' + "=" * 10)
        for crypto in data:
            name = crypto.get('name', 'N/A')
            symbol = crypto.get('symbol', 'N/A').upper()
            price = crypto.get('current_price', 'N/A')
            market_cap = crypto.get('market_cap', 'N/A')
            total_volume = crypto.get('total_volume', 'N/A')
            price_change_24h = crypto.get('price_change_24h', 'N/A')

        print(f"Name: {name}\n Symbol: {symbol}\nPrice(USD): {price}\nMarket Cap: {market_cap}\nTotal Volume: {total_volume}\n Change (24h): {price_change_24h}")
    except Exception as e:
        print("An error occurred while displaying crypto stats:", e)


def filter_by_name(data, keyword):
    try:
        filtered_data = [crypto for crypto in data if keyword.lower() in crypto.get('symbol', '').lower() ]
        return filtered_data
    except Exception as e:
        print("An error occurred while filtering crypto data by name:", e)
        return []


def filter_by_value(data, value):
    try:
        filtered_data = [crypto for crypto in data if crypto.get('current_price', 0) > value]
        return filtered_data
    except Exception as e:
        print("An error occurred while filtering crypto data by value:", e)
        return []

def main():
    keyword = input("Write Cryto name: ")
    value = input("Write  value: ")
    while True:
        try:
            stats = fetch_crypto_stats()
            display_stats(stats)
            if keyword:
                stats = filter_by_name(stats, keyword)
            if value:
                stats = filter_by_value(stats, value)
            print("=" * 39 + 'obout cripto' + "=" * 39)
            display_stats(stats)
        except ValueError:
            print("Invalid input for price filter. Please enter a number.")
        except Exception as e:
            print("An error has occurred", e)

        time.sleep(5)
if __name__ == "__main__":
   main()
