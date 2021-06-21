import requests, time
from CoinbaseClient import Client
from SendMail import SendMail


class PriceChangeBot:
    def __init__(self, currency, price):
        self.client = Client()
        self.currency = currency
        self.price = price
    
    def notify_current_price(self):
        latestPrice = self.client.latest_price(self.currency)
        # Add a way to store the emailing list somewhere
        mail = SendMail(['mason.cable@protonmail.com'])
        if latestPrice['price'] == self.price:
            price = round(float(latestPrice['price']), 2)
            coinData = {
                "currency": self.currency,
                "notification_price": self.price
            }
            mail.send_price_change_alert(coinData)
            return "We will log this in the future"
        