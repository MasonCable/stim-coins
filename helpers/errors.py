import time
import ast

def ip_error(dataStream):
    
    if not 'reason' in dataStream:
        return dataStream
    else:
        message = ast.literal_eval(dataStream['reason'])
        keywords = ['IP', 'whitelist']
        if keywords[0] and keywords[1] in message['message']:
            # return "Please check IP configuration"
            return message['message']

def no_data():
    return "There is no data being returned"

def handle_unknown_error(message):
    return "Unkown Error"
