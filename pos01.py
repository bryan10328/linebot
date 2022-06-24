from functools import cache
from turtle import textinput
from flask import Flask, request, abort
import re
import os
import json
import requests
import mymenu
import client
import time
from linebot import (
    LineBotApi, WebhookHandler
)

from linebot.exceptions import (
    InvalidSignatureError
)
# from linebot.models import (
#     MessageEvent, TextMessage, TextSendMessage,PostbackTemplateAction,CarouselColumn,URITemplateAction,CarouselTemplate,ImagemapSendMessage
# )
from linebot.models import *
#from linebot.models import ConfirmTemplate,PostbackAction,URIAction, MessageAction,FlexSendMessage, MessageTemplateAction,TemplateSendMessage, ButtonsTemplate,ImageCarouselTemplate,ImageCarouselColumn
app = Flask(__name__)
handler = WebhookHandler('150c61e0afd1f4eae2e348a448f53b59')
Users=[]
line_bot_api = LineBotApi('fJePXX8LsMpyKuVtiEJEFqc9u5HHDQwARHXVOwd4pbubcvnbJIADHPJwHH05zRQu6VwKd8UjyqMaGtTnltgxGfkgXqMmxS/RarrZrm4r1u1tVTz5YjueUGiIe5nTNZKcnW3+9E1/KYepnruMhmiZSwdB04t89/1O/w1cDnyilFU=')
menuid=["","","","","","","","","",""]
#menuid[0]=mymenu.menu3x2( "menu","下單功能表",["果汁","花果茶","茶飲","氣泡飲","咖啡","奶茶"],"b1.png")
#menuid[0]=mymenu.basemenu( "menu","下單功能表",["產品分類","取消","確定","訂單預覽"],"posmenu001.jpg")

menuid[0]='richmenu-83fc719b2e69433e8e58e8ad5a37fe13'

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
    #switch(event.message.text,line_id,event.reply_token,profile)
    print(line_id)
#     buttons_template_message = TemplateSendMessage(
#     alt_text='Buttons template',
#     template=ButtonsTemplate(
#         thumbnail_image_url='https://drive.google.com/uc?export=view&id=1CJFfSy6llQ52GE71eKYyxiMWeUmWpVqA',
#         text='果汁類',
#         actions=[
#             MessageTemplateAction(
#                 label='選擇',
#                 text='select 果汁',
#             ) 
#         ]
#     )
# )
 
#     line_bot_api.reply_message(event.reply_token, buttons_template_message)
#     buttons_template_message2 = TemplateSendMessage(
#     alt_text='Buttons template',
#     template=ButtonsTemplate(
#         thumbnail_image_url='https://drive.google.com/uc?export=view&id=1Xu1ApdUIvjOUvno7XbmvznQDNDIwiwp3',
#         text='花果茶類',
#         actions=[
#             MessageTemplateAction(
#                 label='選擇',
#                 text='select 花果茶',
#             ) 
#         ]
#     )
# )
#     line_bot_api.reply_message(event.reply_token, buttons_template_message2)

    # carousel_template_message = TemplateSendMessage(
    #     alt_text='Carousel template',
        
    #     template=CarouselTemplate(
    #         size='small',
    #         columns=[
    #             CarouselColumn(
    #                 thumbnail_image_url='https://drive.google.com/uc?export=view&id=1CJFfSy6llQ52GE71eKYyxiMWeUmWpVqA',
    #                 text='果汁',
    #                 actions=[
    #                     PostbackAction(
    #                         label='選擇',
    #                         display_text='果汁',
    #                         data='action=buy&itemid=1'
    #                     ) 
    #                 ]
    #             ),
    #             CarouselColumn(
    #                 thumbnail_image_url='https://drive.google.com/uc?export=view&id=1Xu1ApdUIvjOUvno7XbmvznQDNDIwiwp3',
    #                 text='花果茶',
    #                 actions=[
    #                     PostbackAction(
    #                         label='選擇',
    #                         display_text='花果茶',
    #                         data='action=buy&itemid=2'
    #                     ) 
    #                 ]
    #             ),
    #             CarouselColumn(
    #                 thumbnail_image_url='https://drive.google.com/uc?export=view&id=1XhtxloJ4VpRs_rNLx9RhTtWOL-vUS0at',
    #                 text='茶飲',
    #                 actions=[
    #                     PostbackAction(
    #                         label='選擇',
    #                         display_text='茶飲',
    #                         data='action=buy&itemid=2'
    #                     ) 
    #                 ]
    #             ),
 
    #             CarouselColumn(
    #                 thumbnail_image_url='https://drive.google.com/uc?export=view&id=1A_tDxPxhIx72RXnshmoPNuYIuJprS-YB',
    #                 text='氣泡飲',
    #                 actions=[
    #                     PostbackAction(
    #                         label='選擇',
    #                         display_text='氣泡飲',
    #                         data='action=buy&itemid=2'
    #                     ) 
    #                 ]
    #             ),
    #             CarouselColumn(
    #                 thumbnail_image_url='https://drive.google.com/uc?export=view&id=1r0nSyye45feUejKbi2g-Ufx9PoS4n0LJ',
    #                 text='咖啡',
    #                 actions=[
    #                     PostbackAction(
    #                         label='選擇',
    #                         display_text='咖啡',
    #                         data='action=buy&itemid=2'
    #                     ) 
    #                 ]
    #             ),
    #             CarouselColumn(
    #                 thumbnail_image_url='https://drive.google.com/uc?export=view&id=18rBnL6Ac0dP8RJ0Y4jyDYgQjMwFRA2WZ',
    #                 text='奶茶',
    #                 actions=[
    #                     PostbackAction(
    #                         label='選擇',
    #                         display_text='奶茶',
    #                         data='action=buy&itemid=2'
    #                     ) 
    #                 ]
    #             )
    #         ]
    #     )
    # )

    # line_bot_api.reply_message(event.reply_token, carousel_template_message)

    imagemap_message = ImagemapSendMessage(
            base_url='https://drive.google.com/uc?export=view&id=11YXnhm2AP8Dx4wkKkbZ6XtJD9ESJ1rjq',
 
            alt_text='this is an imagemap',
            base_size=BaseSize(height=314, width=640),          
            actions=[
                # URIImagemapAction(# 超連結
                #     link_uri='https://marketingliveincode.com/',
                #     area=ImagemapArea(
                #         x=0, y=0, width=520, height=1040
                #     )
                # ),
                MessageImagemapAction(# 文字訊息
                    text='戳我幹嘛！',
                    area=ImagemapArea(
                        x=0, y=0, width=314, height=640
                    )
                )
            ]
        )
    line_bot_api.reply_message(event.reply_token, imagemap_message)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run()