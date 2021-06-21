import requests
from config.creds import MAILGUN_APIKEY

class SendMail():
    def __init__(self, toList):
        # TYPE arr
        self.toList = toList
        self.alertUrl = "https://api.mailgun.net/v3/alert.stimcoins.com/messages"
        self.alertFromAddress = "Stimcoins Alert <mailgun@alert.stimcoins.com>"
        self.mailUrl = "https://api.mailgun.net/v3/mail.stimcoins.com/messages"
        self.mailFromAddress = "Stimcoins Mail <mailgun@alert.stimcoins.com>"
        

    def send_price_change_alert(self, coinData):
        return requests.post(
            self.alertUrl,
            auth=("api", MAILGUN_APIKEY),
            data={"from": self.alertFromAddress,
                  "to": self.toList,
                  "subject": "{} PRICE NOTIFICATION".format(coinData['currency']),
                  "text": "{0} has reached the price of {1}, would you like to place a buy or sell order?".format(coinData['currency'], coinData['notification_price'])

            })

    def send_welcome_email(self):
        return requests.post(
            self.mailUrl,
            auth=("api", MAILGUN_APIKEY),
            data={"from": self.mailFromAddress,
                    "to": self.toList,
                    "subject": 'Stimcoins test email',
                    "text": "Welcome to stimcoins, if you have any questions please click <a href='{0}'>Here</a>".format('https://www.stimcoins.com/help')
                })

    
