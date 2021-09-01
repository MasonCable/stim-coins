import requests, time, math
import openpyxl
from SendMail import SendMail
from helpers.algo import get_change
from ClientFunctions import ClientFunctions
from CoinbaseClient import Client
from GenerateReport import *

class Bot:
    def __init__(self, dataObject):
        self.dataObject = dataObject
        self.functions = ClientFunctions()
        self.client = Client()
        
        # This is a list of dict with productId as key and price as value
        self.averageBuyPrice = []

    
    def analyze(self):
        """
                EXAMPLE RESPONSE            {'type': 'ticker',            'sequence': 27663632374,             'product_id': 'BTC-USD',             'price': '34539.98',             'open_24h': '34129.28',             'volume_24h': '8533.66530825',             'low_24h': '33867.85',             'high_24h': '34837.08',             'volume_30d': '324271.28515124',             'best_bid': '34539.98',             'best_ask': '34544.83',             'side': 'sell',             'time': '2021-07-25T21:53:49.012386Z',             'trade_id': 196254869,            'last_size': '0.00104721'} 
        """
        currency = self.dataObject['product_id']
        
        if self.functions.isHolding(currency):            
            self.isHolding(currency)            
        else:            
            print('We do not own {} ----------- drop data for now'.format(currency))
            
            
        
    

    # Main Function to check for what to do with an owned asset
    def isHolding(self, currency): 
        currencyName = currency[:currency.index('-')]
        buyPrice = self.functions.buy_price(currencyName)
        currentPrice = self.dataObject['price']
        # self.priceDifference(buyPrice)
        currentPrice = self.dataObject['price']
        priceChange = get_change(float(currentPrice), float(buyPrice))
        
        isDown=''
        if priceChange > 0.0:
            isDown='UP'
        else: 
            isDown='DOWN'
        priceObject = { "current_price": currentPrice, "buy_price": buyPrice , "price_difference": priceChange, "currency": currencyName, "is_down": isDown }
        
        self.potentialSell(priceObject) 
    
    def potentialSell(self, priceObject):
        priceDifference = priceObject['price_difference']
        roundedPriceDiff = round(priceDifference, 2)
        isDown= priceObject['is_down']
        coinData = { "currency": priceObject['currency'] ,"up_or_down": isDown, "price_difference": roundedPriceDiff }
        print(priceObject)
        # if roundedPriceDiff > 6:
        #     SendMail(['mason.cable@protonmail.com']).send_price_change_alert(coinData)
        #     print("Email Sent")
        

    
    def createBuySignal(self, coinData):
        pass
    
    
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