import requests
import json



url = "https://api.telegram.org/bot1436762952:AAH_wZSSzhGM_RiLNy6spuc2vfTBDAwGauY/"

def sendmessage(chatid,text):
    params = {'chat_id' : chatid , 'text' : text}
    response = requests.post(url+'sendmessage',data=params)
    return response
def getupdates():
    response = requests.get(url+'getupdates')
