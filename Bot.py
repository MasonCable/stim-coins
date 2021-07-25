import requests, time
from CoinbaseClient import Client
from SendMail import SendMail


class Bot:
    def __init__(self, dataObject):
        self.dataObject = dataObject

    
    def analyze(self):
        pass