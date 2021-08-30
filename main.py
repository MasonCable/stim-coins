import time, requests
from argparse import ArgumentParser
from CoinbaseClient import Client
from ClientFunctions import ClientFunctions
from Bot import Bot
from SendMail import SendMail
import openpyxl
from WebsocketClient import WebsocketClient


parser = ArgumentParser(description="This service is only for smart notifications, if you want to use an automated trading bot please check out our website https://stimcoins.com")

parser.add_argument("-nl", "--notification-list", help="List of users that will recieve email notifications for price changes. Seperate email addresses with commas.")
parser.add_argument("-dr", "--daily-report", help="Email users a daily report of all price changes.")
parser.add_argument("-m", "--main", action='store_true', help="Run the main program loop")
parser.add_argument("-t", "--test", action='store_true',help="Run whateber is in the test() function")


args = parser.parse_args()

tickerData = [{'type': 'ticker', 'sequence': 344843567, 'product_id': 'DOGE-USD', 'price': '0.2034', 'open_24h': '0.2043', 'volume_24h': '106604787.40000000', 'low_24h': '0.2016', 'high_24h': '0.2099', 'volume_30d': '5072583443.60000000', 'best_bid': '0.2034', 'best_ask': '0.2036', 'side': 'sell', 'time': '2021-08-02T23:55:08.571850Z', 'trade_id': 6478665, 'last_size': '745.7'}, 
{'type': 'ticker', 'sequence': 344843841, 'product_id': 'DOGE-USD', 'price': '0.2036', 'open_24h': '0.2043', 'volume_24h': '106604836.40000000', 'low_24h': '0.2016', 'high_24h': '0.2099', 'volume_30d': '5072583492.60000000', 'best_bid': '0.2035', 'best_ask': '0.2036', 'side': 'buy', 'time': '2021-08-02T23:55:14.647274Z', 'trade_id': 6478666, 'last_size': '49'}, 
{'type': 'ticker', 'sequence': 344844153, 'product_id': 'DOGE-USD', 'price': '0.2035', 'open_24h': '0.2043', 'volume_24h': '106604902.70000000', 'low_24h': '0.2016', 'high_24h': '0.2099', 'volume_30d': '5072583558.90000000', 'best_bid': '0.2035', 'best_ask': '0.2037', 'side': 'sell', 'time': '2021-08-02T23:55:22.427288Z', 'trade_id': 6478667, 'last_size': '66.3'}, 
{'type': 'ticker', 'sequence': 344844194, 'product_id': 'DOGE-USD', 'price': '0.2037', 'open_24h': '0.2043', 'volume_24h': '106605137.60000000', 'low_24h': '0.2016', 'high_24h': '0.2099', 'volume_30d': '5072583793.80000000', 'best_bid': '0.2035', 'best_ask': '0.2037', 'side': 'buy', 'time': '2021-08-02T23:55:23.285589Z', 'trade_id': 6478668, 'last_size': '234.9'}, 
{'type': 'ticker', 'sequence': 344844235, 'product_id': 'DOGE-USD', 'price': '0.2037', 'open_24h': '0.2043', 'volume_24h': '106609825.80000000', 'low_24h': '0.2016', 'high_24h': '0.2099', 'volume_30d': '5072588482.00000000', 'best_bid': '0.2035', 'best_ask': '0.2037', 'side': 'buy', 'time': '2021-08-02T23:55:25.458396Z', 'trade_id': 6478669, 'last_size': '4688.2'}, 
{'type': 'ticker', 'sequence': 344844237, 'product_id': 'DOGE-USD', 'price': '0.2037', 'open_24h': '0.2043', 'volume_24h': '106609950.60000000', 'low_24h': '0.2016', 'high_24h': '0.2099', 'volume_30d': '5072588606.80000000', 'best_bid': '0.2035', 'best_ask': '0.2037', 'side': 'buy', 'time': '2021-08-02T23:55:25.458396Z', 'trade_id': 6478670, 'last_size': '124.8'}, 
{'type': 'ticker', 'sequence': 344844269, 'product_id': 'DOGE-USD', 'price': '0.2037', 'open_24h': '0.2043', 'volume_24h': '106609960.20000000', 'low_24h': '0.2016', 'high_24h': '0.2099', 'volume_30d': '5072588616.40000000', 'best_bid': '0.2035', 'best_ask': '0.2037', 'side': 'buy', 'time': '2021-08-02T23:55:27.282588Z', 'trade_id': 6478671, 'last_size': '9.6'}]



functions = ClientFunctions()
client = Client()
productList = ['ETH-USD', 'BTC-USD', 'DOGE-USD', 'LTC-USD']

def test_functions():
    buy = functions.buy_price('DOGE')
    return buy

def test_email():
    toList = ['mason.cable@protonmail.com']
    mailer = SendMail(toList)

    return mailer.send_welcome_email()

def main():
    wsClient = WebsocketClient(url="wss://ws-feed.pro.coinbase.com", products=productList, channels=['ticker'])
    wsClient.start()

def test():
    for i in functions.open_accounts():
        print("{}\n".format(i))
    


if __name__ == "__main__":
    if args.main:
        main()
    elif args.test:
        test()
    else:
        print("Please specify how you want to run this script\n -m for the main loop\n -t for the test() function")
    
            
            
        


    