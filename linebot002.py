from flask import Flask, request, abort
import re
import os
import json
import requests
import menubody
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

from linebot.models import ConfirmTemplate,PostbackAction,URIAction, MessageAction,FlexSendMessage, MessageTemplateAction,TemplateSendMessage, ButtonsTemplate,ImageCarouselTemplate,ImageCarouselColumn
app = Flask(__name__)
line_bot_api = LineBotApi('fJePXX8LsMpyKuVtiEJEFqc9u5HHDQwARHXVOwd4pbubcvnbJIADHPJwHH05zRQu6VwKd8UjyqMaGtTnltgxGfkgXqMmxS/RarrZrm4r1u1tVTz5YjueUGiIe5nTNZKcnW3+9E1/KYepnruMhmiZSwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('150c61e0afd1f4eae2e348a448f53b59')
 
headers = {"Authorization":"Bearer fJePXX8LsMpyKuVtiEJEFqc9u5HHDQwARHXVOwd4pbubcvnbJIADHPJwHH05zRQu6VwKd8UjyqMaGtTnltgxGfkgXqMmxS/RarrZrm4r1u1tVTz5YjueUGiIe5nTNZKcnW3+9E1/KYepnruMhmiZSwdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}

def basemenu(userid):
  body=menubody.menu3x2("menu","類別",["果汁","花果茶","茶飲","氣泡飲","咖啡","奶茶"])
  menubody.transfer(userid,body,"b2.jpg")
 

basemenu("")
 
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    json_object = json.loads(body)
 
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_id = event.source.user_id
    profile = line_bot_api.get_profile(line_id)
    switch(event.message.text,line_id)
    print(line_id)
 
def switch(text,userid):
    match text:
        case '果汁':
            body=menubody.menu3x2("juice","果汁",["奇異果","葡萄汁","蔓越莓","藍莓","百香果","↵(果汁)"])
            menubody.transfer(userid,body,"juice001.jpg")
            return "果汁"
        case '花果茶':
            body=menubody.menu3x2("scentedtea","花果茶",["洛神花茶","玫瑰花茶","蘋果茶","水果茶","花茶","↵(花果茶)"])
            menubody.transfer(userid,body,"scentedtea001.jpg")
            return "花果茶"
        case '茶飲':
            body=menubody.menu3x2("tea","茶飲",["抹茶拿鐵","青心烏龍","檸檬紅茶","普洱","茉香綠茶","↵(茶飲)"])
            menubody.transfer(userid,body,"tea001.jpg")
            return "茶飲"
        case '氣泡飲':
            body=menubody.menu3x2("sparkling","氣泡飲",["天使之淚","末日黃昏","蘋紛秋色","莓飛色舞","浪漫紫幻","↵(氣泡飲)"])
            menubody.transfer(userid,body,"sparkling001.jpg")
            return "氣泡飲"
        case '咖啡':
            body=menubody.menu4x1("coffee","咖啡",["美式","拿鐵","濃縮","↵(咖啡)"])
            menubody.transfer(userid,body,"coffee001.jpg")
            return "咖啡"
        case '奶茶':
            body=menubody.menu3x2("milktea","奶茶",["綠奶","阿薩姆","烏龍奶茶","烏龍奶茶","烏龍奶茶","↵(奶茶)"])
            menubody.transfer(userid,body,"milktea001.jpg")
            return "奶茶"
        case '↵(咖啡)':
            basemenu(userid)
            return "↵(咖啡)"
        case '↵(奶茶)':
            basemenu(userid)
            return "↵(奶茶)"
        case '↵(果汁)':
            basemenu(userid)
            return "↵(果汁)"
        case '↵(花果茶)':
            basemenu(userid)
            return "↵(花果茶)"
        case '↵(茶飲)':
            basemenu(userid)
            return "↵(茶飲)"
        case '↵(氣泡飲)':
            basemenu(userid)
            return "↵(氣泡飲)"

 

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run()
#app.run(host='127.0.0.1', port=port)