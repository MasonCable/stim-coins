import requests, time
from CoinbaseClient import Client
from SendMail import SendMail
from ClientFunctions import ClientFunctions


class Bot:
    def __init__(self, dataObject):
        self.dataObject = dataObject
        self.functions = ClientFunctions()

    
    def analyze(self):
        """
                EXAMPLE RESPONSE
            {'type': 'ticker',
            'sequence': 27663632374,
             'product_id': 'BTC-USD',
             'price': '34539.98',
             'open_24h': '34129.28',
             'volume_24h': '8533.66530825',
             'low_24h': '33867.85',
             'high_24h': '34837.08',
             'volume_30d': '324271.28515124',
             'best_bid': '34539.98',
             'best_ask': '34544.83',
             'side': 'sell',
             'time': '2021-07-25T21:53:49.012386Z',
             'trade_id': 196254869,
             'last_size': '0.00104721'} 
        """
        currency = self.dataObject['product_id']
        transactionData = self.most_recent_transactions(currency)
        
        # Check current holdings for currency X
            # check if I own currency
                # If I own currency check my average buy price
                    # If current price is x% higher than average buy price
                        # Do X
                    # Else
                        # Do X
                # If I dont own currency check last time sold and store previousSell
        

    def find_average_ask(self, currency, timePeriod):
        pass

    def most_recent_transactions(self, currency):
        mostRecentBuy = self.functions.most_recent_buy(currency)
        mostRecentSell = self.functions.most_recent_sell(currency)
        transactionData = {
            "sell": mostRecentSell,
            "buy": mostRecentBuy
        }

        return transactionData
        