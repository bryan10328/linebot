from flask import Flask, request, abort
import re
import os
import json
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

from linebot.models import ConfirmTemplate,PostbackAction,URIAction, MessageAction,FlexSendMessage, MessageTemplateAction,TemplateSendMessage, ButtonsTemplate,ImageCarouselTemplate,ImageCarouselColumn
app = Flask(__name__)
line_bot_api = LineBotApi('fJePXX8LsMpyKuVtiEJEFqc9u5HHDQwARHXVOwd4pbubcvnbJIADHPJwHH05zRQu6VwKd8UjyqMaGtTnltgxGfkgXqMmxS/RarrZrm4r1u1tVTz5YjueUGiIe5nTNZKcnW3+9E1/KYepnruMhmiZSwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('150c61e0afd1f4eae2e348a448f53b59')

# line_bot_api.push_message('U8e983edaa28a2abb6d66e74d273e7edb', FlexSendMessage(
#     alt_text='hello',
#     contents={
#       "type": "bubble",
#       "hero": {
#         "type": "image",
#         "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
#         "size": "full",
#         "aspectRatio": "20:13",
#         "aspectMode": "cover",
#         "action": {
#           "type": "uri",
#           "uri": "http://linecorp.com/"
#         }
#       },
#       "body": {
#         "type": "box",
#         "layout": "vertical",
#         "contents": [
#           {
#             "type": "text",
#             "text": "Brown Cafe",
#             "weight": "bold",
#             "size": "xl"
#           },
#           {
#             "type": "box",
#             "layout": "baseline",
#             "margin": "md",
#             "contents": [
#               {
#                 "type": "icon",
#                 "size": "sm",
#                 "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
#               },
#               {
#                 "type": "icon",
#                 "size": "sm",
#                 "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
#               },
#               {
#                 "type": "icon",
#                 "size": "sm",
#                 "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
#               },
#               {
#                 "type": "icon",
#                 "size": "sm",
#                 "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
#               },
#               {
#                 "type": "icon",
#                 "size": "sm",
#                 "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
#               },
#               {
#                 "type": "text",
#                 "text": "4.0",
#                 "size": "sm",
#                 "color": "#999999",
#                 "margin": "md",
#                 "flex": 0
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "vertical",
#             "margin": "lg",
#             "spacing": "sm",
#             "contents": [
#               {
#                 "type": "box",
#                 "layout": "baseline",
#                 "spacing": "sm",
#                 "contents": [
#                   {
#                     "type": "text",
#                     "text": "Place",
#                     "color": "#aaaaaa",
#                     "size": "sm",
#                     "flex": 1
#                   },
#                   {
#                     "type": "text",
#                     "text": "Miraina Tower, 4-1-6 Shinjuku, Tokyo",
#                     "wrap": True,
#                     "color": "#666666",
#                     "size": "sm",
#                     "flex": 5
#                   }
#                 ]
#               },
#               {
#                 "type": "box",
#                 "layout": "baseline",
#                 "spacing": "sm",
#                 "contents": [
#                   {
#                     "type": "text",
#                     "text": "Time",
#                     "color": "#aaaaaa",
#                     "size": "sm",
#                     "flex": 1
#                   },
#                   {
#                     "type": "text",
#                     "text": "10:00 - 23:00",
#                     "wrap": True,
#                     "color": "#666666",
#                     "size": "sm",
#                     "flex": 5
#                   }
#                 ]
#               }
#             ]
#           }
#         ]
#       },
#       "footer": {
#         "type": "box",
#         "layout": "vertical",
#         "spacing": "sm",
#         "contents": [
#           {
#             "type": "button",
#             "style": "link",
#             "height": "sm",
#             "action": {
#               "type": "uri",
#               "label": "CALL",
#               "uri": "https://linecorp.com"
#             }
#           },
#           {
#             "type": "button",
#             "style": "link",
#             "height": "sm",
#             "action": {
#               "type": "uri",
#               "label": "WEBSITE",
#               "uri": "https://linecorp.com"
#             }
#           },
#           {
#             "type": "box",
#             "layout": "vertical",
#             "contents": [],
#             "margin": "sm"
#           }
#         ],
#         "flex": 0
#       }
#     }
# ))Bearer ?????? Access Token
 
headers = {"Authorization":"Bearer fJePXX8LsMpyKuVtiEJEFqc9u5HHDQwARHXVOwd4pbubcvnbJIADHPJwHH05zRQu6VwKd8UjyqMaGtTnltgxGfkgXqMmxS/RarrZrm4r1u1tVTz5YjueUGiIe5nTNZKcnW3+9E1/KYepnruMhmiZSwdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}

#headers = {'Authorization':'Bearer ?????? access token','Content-Type':'application/json'}

body = {
    'size': {'width': 2500, 'height': 1200},   # ????????????
    'selected': 'true',                        # ??????????????????
    'name': 'aaa',                             # ???????????? ( ?????? Alias Id )
    'chatBarText': '?????? A',                    # ????????? LINE ???????????????
    'areas':[                                  # ????????????
        {
          'bounds': {'x': 0, 'y': 0, 'width': 830, 'height': 280},
          'action': {'type': 'postback', 'data':'no-data'}          # ?????? A ?????? postback
        },
        {
          'bounds': {'x': 835, 'y': 0, 'width':830, 'height': 640},
          'action': {'type': 'richmenuswitch', 'richMenuAliasId': 'bbb', 'data':'change-to-bbb'} # ?????? B ?????? richmenuswitch
        },
        {
          'bounds': {'x': 1670, 'y': 0, 'width':830, 'height': 640},
          'action': {'type': 'richmenuswitch', 'richMenuAliasId': 'ccc', 'data':'change-to-ccc'} # ?????? C ?????? richmenuswitch
        }
    ]
  }
req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu',
                      headers=headers,data=json.dumps(body).encode('utf-8'))
ss=req.text.split('"')

print(ss[3])
 
req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/'+ss[3], headers=headers)
print(req.text)
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    print(body)
    
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # line_bot_api.reply_message(
    #     event.reply_token,
    #     TextSendMessage(text=event.message.text))
    # profile = line_bot_api.get_profile(event.source.user_id)
    # line_bot_api.reply_message(
    #         event.reply_token, [
    #             TextSendMessage(text='Display name: ' + profile.display_name),
    #             TextSendMessage(text='UserID: ' + profile.user_id),
    #             TextSendMessage(text='Status message: ' + str(profile.status_message))
    #         ]
    #     )
    buttons_template_message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            title='Menu',
            text='???????????????',
            actions=[
                MessageTemplateAction(
                    label='?????????',
                    text='option one',
                ),
                MessageTemplateAction(
                    label='option two',
                    text='?????????',
                )
            ]
        )
    )
 

    line_bot_api.reply_message(event.reply_token, buttons_template_message)
    # message = text=event.message.text
    # if re.match('123',message):
    #      print('???????????????')
    #      image_carousel_template_message = TemplateSendMessage(
    #          alt_text='??????????????????',
    #          template=ImageCarouselTemplate(
    #              columns=[
    #                  ImageCarouselColumn(
    #                      image_url='https://i.imgur.com/wpM584d.jpg',
    #                      action=PostbackAction(
    #                          label='Python??????????????????',
    #                          display_text='?????????????????????',
    #                          data='action=???????????????????????????????????????????????????'
    #                      )
    #                  ),
    #                  ImageCarouselColumn(
    #                      image_url='https://i.imgur.com/W7nI6fg.jpg',
    #                      action=PostbackAction(
    #                          label='LineBot???????????????',
    #                          display_text='????????????????????????????????????',
    #                          data='action=???????????????????????????????????????????????????'
    #                      )
    #                  )
    #              ]
    #          )
    #      )
    #      line_bot_api.reply_message(event.reply_token, image_carousel_template_message)
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run()
#app.run(host='127.0.0.1', port=port)