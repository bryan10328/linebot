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
def menu3x2(d1,d2,strdata):
  body = {
    "size": {"width": 1200, "height": 772},
    "selected": "true",
    "name": "menu",
    "chatBarText": "類別",
    "areas":[
        {
          "bounds": {"x": 0, "y": 0, "width": 400, "height": 386},
          "action": {"type": "message", "text": strdata[0]}
        },
        {
          "bounds": {"x": 400, "y": 0, "width": 400, "height": 386},
          "action": {"type": "message", "text": strdata[1]}
        },
        {
          "bounds": {"x": 800, "y": 0, "width": 400, "height": 386},
          "action": {"type": "message", "text": strdata[2]}
        },
        {
          "bounds": {"x": 0, "y": 386, "width": 400, "height": 386},
          "action": {"type": "message", "text": strdata[3]}
        },
        {
          "bounds": {"x": 400, "y": 386, "width": 400, "height": 386},
          "action": {"type": "message", "text": strdata[4]}
        },
        {
          "bounds": {"x": 800, "y": 386, "width": 400, "height": 386},
          "action": {"type": "message", "text": strdata[5]}
        } 
          
        
     
    ]
 
  }
  return body
def orders(d1,d2,strdata):
  a=0
def menu4x1(d1,d2,strdata):
  body = {
    "size": {"width": 1600, "height": 360},
    "selected": "true",
    "name": d1,
    "chatBarText": d2,
    "areas":[
       
        {
          "bounds": {"x": 0, "y": 66, "width": 400, "height": 360},
          "action": {"type": "message", "text":  strdata[0]}
        },
        {
          "bounds": {"x": 400, "y": 66, "width": 400, "height": 360},
          "action": {"type": "message", "text":  strdata[1]}
        },
        {
          "bounds": {"x": 800, "y": 66, "width": 400, "height": 360},
          "action": {"type": "message", "text":  strdata[2]}
        } ,
         {
          "bounds": {"x": 1200, "y": 0, "width": 400, "height": 360},
          "action": {"type": "message", "text": strdata[3]}
        }
    ]
  }
  return body
def transfer(userid,body,pic):
  req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu',
                      headers=headers,data=json.dumps(body).encode('utf-8'))
  ss=req.text.split('"')
  print(ss[3])
  with open(pic, 'rb') as f:
    line_bot_api.set_rich_menu_image(ss[3], "image/jpeg", f)
  req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/'+ss[3], headers=headers,data=json.dumps(body).encode('utf-8')) 
  if(len(userid)>1):
    line_bot_api.link_rich_menu_to_user(userid,ss[3])