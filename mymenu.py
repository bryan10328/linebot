import json
from turtle import title
import requests
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
headers = {"Authorization":"Bearer fJePXX8LsMpyKuVtiEJEFqc9u5HHDQwARHXVOwd4pbubcvnbJIADHPJwHH05zRQu6VwKd8UjyqMaGtTnltgxGfkgXqMmxS/RarrZrm4r1u1tVTz5YjueUGiIe5nTNZKcnW3+9E1/KYepnruMhmiZSwdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}
line_bot_api = LineBotApi('fJePXX8LsMpyKuVtiEJEFqc9u5HHDQwARHXVOwd4pbubcvnbJIADHPJwHH05zRQu6VwKd8UjyqMaGtTnltgxGfkgXqMmxS/RarrZrm4r1u1tVTz5YjueUGiIe5nTNZKcnW3+9E1/KYepnruMhmiZSwdB04t89/1O/w1cDnyilFU=')
def basemenu(d1,d2,strdata,pic):
  body = {
    "size": {"width": 1200, "height": 380},
    "selected": "true",
    "name": d1,
    "chatBarText": d2,
    "areas":[
        {
          "bounds": {"x": 48, "y": 120, "width": 240, "height": 240},
          "action": {"type": "message", "text": strdata[0]}
        },
        {
          "bounds": {"x": 336, "y": 120, "width": 240, "height": 240},
          "action": {"type": "message", "text": strdata[1]}
        } ,
        {
          "bounds": {"x": 624, "y": 120, "width": 240, "height": 240},
          "action": {"type": "message", "text": strdata[2]}
        } ,
        {
          "bounds": {"x": 912, "y": 120, "width": 240, "height": 240},
          "action": {"type": "message", "text": strdata[3]}
        } 
    ]
  }
  return transfer(body,pic)

def transfer(body,pic):
  req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu',
                      headers=headers,data=json.dumps(body).encode('utf-8'))
  ss=req.text.split('"')
  print(ss[3])
  with open(pic, 'rb') as f:
    try:
      line_bot_api.set_rich_menu_image(ss[3], "image/jpeg", f)
       
    except Exception as e:
        a=0
        print(str(e))
  req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/'+ss[3], headers=headers,data=json.dumps(body).encode('utf-8')) 
  return ss[3]