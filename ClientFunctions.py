import time, requests, math
from CoinbaseClient import Client

class ClientFunctions(Client):
    def __init__(self):
        self.client = Client()

    def isHolding(self, currency):
        holds = self.client.account_holds()
        for i in holds:
            if i['currency'] == currency:
                return True
        return False

    # CB does not offer a watchlit route in pro so we get a list based off of all previos orders
    def watchlist(self):
        # If user does not have any previos orders we create a watchlist for them 
        if len(self.client.orders('done')) < 1:
            return ["BTC", "ETH", "LTC", "DOGE"]
            
        watchlist=[]
        for i in self.client.orders('done'):
            myStr = i['product_id']
            idx = myStr.index('-')
            currencyName = myStr[:idx]
            if currencyName not in watchlist:
                watchlist.append(currencyName)
        
        for i in self.open_accounts():
            if i['currency'] not in watchlist and i['currency'] != 'USD':
                watchlist.append(i['currency'])

        return watchlist

    # Return all accounts with a balance
    def open_accounts(self):
        accounts=[]
        for i in self.client.accounts():
            if float(i['available']) != 0:
                accounts.append(i)
        return accounts

    # Returns the most recent buy for a given currency
    def most_recent_buy(self, currency):
        completedOrders = self.client.orders('done')
        product = "{}-USD".format(currency)
        
        for i in completedOrders:
            try:
                if i['product_id'] == product and i['side'] == 'buy':
                    return i
            except:
                return completedOrders

    #  Returns Bool
    def does_own(self, currency):
        pass
    

    # Returns the most recent sell for a given currency
    def most_recent_sell(self,currency):
        completedOrders = self.client.orders('done')
        product = "{}-USD".format(currency)

        try:
            for i in completedOrders:
                if i['product_id'] == product and i['side'] == 'sell':
                    return i
        except:
            return completedOrders
    
    # Get latest buy price for a currency
    def buy_price(self, currency):
        buy = self.most_recent_buy(currency)
        
        try:
            return buy['price']
        except:
            try:                
                cost = round(float(buy['funds']), 2)
                size = round(float(buy['filled_size']), 7)            
                buyPrice = round(cost/size, 2)

                return buyPrice

            except:
                return buy

        
            

