import time, requests
from MarketData import MarketData
from CoinAccount import Account
from auth_clientu import CBAuth
from auth_credentials import PASSPHRASE, KEY, SECRET
from urls import *

# Global variables
auth = CBAuth(KEY, SECRET, PASSPHRASE)
accountData = Account()

class Test(MarketData):
    def test_auth(self):

