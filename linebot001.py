from flask import Flask, request, abort
import re
import os
import json
import menu_body
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,FlexSendMessage,
)
from linebot.models import PostbackAction,URIAction, MessageAction, TemplateSendMessage, ButtonsTemplate,ImageCarouselTemplate,ImageCarouselColumn
app = Flask(__name__)
line_bot_api = LineBotApi('fJePXX8LsMpyKuVtiEJEFqc9u5HHDQwARHXVOwd4pbubcvnbJIADHPJwHH05zRQu6VwKd8UjyqMaGtTnltgxGfkgXqMmxS/RarrZrm4r1u1tVTz5YjueUGiIe5nTNZKcnW3+9E1/KYepnruMhmiZSwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('150c61e0afd1f4eae2e348a448f53b59')
menuid=["","","","","","","","","",""]
#menuid[8]=menu_body.count("count","數量",["上一頁","-1","+1","確定"],"count001.jpg")
#line_bot_api.set_default_rich_menu('richmenu-17de6bb11575abe7227a85fdbefbad96')
# try:
#         line_bot_api.set_default_rich_menu('richmenu-e1a763ec12dc96222cb2d8528ea12ac1')
# except  Exception as e:
#     a=0

#FlexMessage = json.load(open('a1.json','r',encoding='utf-8'))
 
# line_bot_api.push_message('U8e983edaa28a2abb6d66e74d273e7edb', FlexSendMessage('profile',FlexMessage))
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    print(body)
    #line_bot_api.reply_message(event.reply_token, TextSendMessage(message))
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
    message = text=event.message.text
    
    line_bot_api.link_rich_menu_to_user(event.source.user_id,'8f901df347c0a6c4124762cd4681649b')
    # if re.match('123',message):
    #     line_bot_api.reply_message(event.reply_token, image_carousel_template_message)
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run()
#app.run(host='127.0.0.1', port=port)