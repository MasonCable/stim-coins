import requests, time
from CoinbaseClient import Client
from SendMail import SendMail
from ClientFunctions import ClientFunctions


class Bot:
    def __init__(self, dataObject):
        self.dataObject = dataObject
        self.functions = ClientFunctions()

    
    def analyze(self):
        currency = self.dataObject['currency']
        transactionData = self.most_recent_transactions(currency)
        # Check current holdings for currency X
            # check if I own currency
                # If I own currency check my average buy price
                    # If current price is x% higher than average buy price
                        # Do X
                    # Else
                        # Do X
                # If I dont own currency check last time sold and store previousSell
                

    
    def most_recent_transactions(self, currency):
        mostRecentBuy = self.functions.most_recent_buy(currency)
        mostRecentSell = self.functions.most_recent_sell(currency)
        transactionData = {
            "sell": mostRecentSell,
            "buy": mostRecentBuy
        }

        return transactionData
        