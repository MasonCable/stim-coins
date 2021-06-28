import time, requests
from argparse import ArgumentParser
from CoinbaseClient import Client
from ClientFunctions import ClientFunctions
from PriceChangeBot import PriceChangeBot
import openpyxl
from WebsocketClient import WebsocketClient


parser = ArgumentParser(description="This service is only for smart notifications, if you want to use an automated trading bot please check out our website https://stimcoins.com")

parser.add_argument("-nl", "--notification-list", help="List of users that will recieve email notifications for price changes. Seperate email addresses with commas.")
parser.add_argument("-dr", "--daily-report", help="Email users a daily report of all price changes.")


args = parser.parse_args()


functions = ClientFunctions()
client = Client()


def test_runs():
    buy = functions.buy_price('DOGE')
    # buy = functions.buy_price('ETH')
    return buy


if __name__ == "__main__":
    # wsClient = WebsocketClient(url="wss://ws-feed.pro.coinbase.com", products='ETH-USD', channels=['ticker'])
    # wsClient.start()
    print(test_runs())
            
            
        


    