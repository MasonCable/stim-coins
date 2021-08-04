import requests, time
import openpyxl
from SendMail import SendMail
from ClientFunctions import ClientFunctions
from CoinbaseClient import Client
from GenerateReport import *

class Bot:
    def __init__(self, dataObject):
        self.dataObject = dataObject
        self.functions = ClientFunctions()
        self.client = Client()
        self.coinsOwned = []
        

    
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
        
        # Is the current currency being held @Bool
        if self.functions.isHolding(currency):
            # Get the current ammount being held and the cost basis
            # holdingData = self.functions.holding_data(currency)
            print('\n WE OWN THIS SHIT')
        else:
            # Was there a previous sell ? When?
            print('\n WE DO NOT OWN THIS SHIT')
            
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
    
    # This function takes in a currency object as seen in the analyze() function
        # tickerObject=Dict -> currency=Str -> storeAll -> Bool 
            # the store all variable lets the function know wether to ignore everything except currency
    def store_data(self, tickerObject, currency, storeAll):
        headers = ['id', 'sequence', 'currency', 'order_type', 'price', 'size', 'best_bid', 'best_ask', 'low_24h','high_24h']
        excelRowData={
            "id": int(tickerObject['trade_id']),
            "sequence": int(tickerObject['sequence']),
            "currency": tickerObject['product_id'],
            "order_type": tickerObject['order_type'],
            "price": float(tickerObject['price']),
            "size": float(tickerObject['last_size']),
            "best_bid": float(tickerObject['best_bid']),
            "best_ask": float(tickerObject['best_ask']),
            "low_24h": float(tickerObject['low_24h']),
            "high_24h": float(tickerObject['high_24h'])
        }

        

    
        #     """
        #         EXAMPLE RESPONSE
        #     {'type': 'ticker',
        #     'sequence': 27663632374,
        #      'product_id': 'BTC-USD',
        #      'price': '34539.98',
        #      'open_24h': '34129.28',
        #      'volume_24h': '8533.66530825',
        #      'low_24h': '33867.85',
        #      'high_24h': '34837.08',
        #      'volume_30d': '324271.28515124',
        #      'best_bid': '34539.98',
        #      'best_ask': '34544.83',
        #      'side': 'sell',
        #      'time': '2021-07-25T21:53:49.012386Z',
        #      'trade_id': 196254869,
        #      'last_size': '0.00104721'} 
        # """