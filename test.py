from flask import Flask, request, abort
import re
import os
import json
import requests
import unittest
import responses
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
     URITemplateAction,
    RichMenu, RichMenuSize, RichMenuArea, RichMenuBounds
)
 
from linebot.models.actions import RichMenuSwitchAction
from linebot.models import ConfirmTemplate,PostbackAction,URIAction, MessageAction,FlexSendMessage, MessageTemplateAction,TemplateSendMessage, ButtonsTemplate,ImageCarouselTemplate,ImageCarouselColumn
app = Flask(__name__)
line_bot_api = LineBotApi('fJePXX8LsMpyKuVtiEJEFqc9u5HHDQwARHXVOwd4pbubcvnbJIADHPJwHH05zRQu6VwKd8UjyqMaGtTnltgxGfkgXqMmxS/RarrZrm4r1u1tVTz5YjueUGiIe5nTNZKcnW3+9E1/KYepnruMhmiZSwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('150c61e0afd1f4eae2e348a448f53b59')

 
 
headers = {"Authorization":"Bearer fJePXX8LsMpyKuVtiEJEFqc9u5HHDQwARHXVOwd4pbubcvnbJIADHPJwHH05zRQu6VwKd8UjyqMaGtTnltgxGfkgXqMmxS/RarrZrm4r1u1tVTz5YjueUGiIe5nTNZKcnW3+9E1/KYepnruMhmiZSwdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}

#headers = {'Authorization':'Bearer 你的 access token','Content-Type':'application/json'}

body = {
    'size': {'width': 2500, 'height': 1200},   # 設定尺寸
    'selected': 'true',                        # 預設是否顯示
    'name': 'aaa',                             # 選單名稱 ( 別名 Alias Id )
    'chatBarText': '選單 A',                    # 選單在 LINE 顯示的標題
    'areas':[                                  # 選單內容
        {
          'bounds': {'x': 0, 'y': 0, 'width': 830, 'height': 280},
          'action': {'type': 'postback', 'data':'no-data'}          # 按鈕 A 使用 postback
        },
        {
          'bounds': {'x': 835, 'y': 0, 'width':830, 'height': 640},
          'action': {'type': 'richmenuswitch', 'richMenuAliasId': 'bbb', 'data':'change-to-bbb'} # 按鈕 B 使用 richmenuswitch
        },
        {
          'bounds': {'x': 1670, 'y': 0, 'width':830, 'height': 640},
          'action': {'type': 'richmenuswitch', 'richMenuAliasId': 'ccc', 'data':'change-to-ccc'} # 按鈕 C 使用 richmenuswitch
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
  
    buttons_template_message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            title='Menu',
            text='請選擇地區',
            actions=[
                MessageTemplateAction(
                    label='選項一',
                    text='option one',
                ),
                MessageTemplateAction(
                    label='option two',
                    text='選項二',
                )
            ]
        )
    )
 

    line_bot_api.reply_message(event.reply_token, buttons_template_message)
 #######################################
class TestLineBotApi(unittest.TestCase):
    maxDiff = None

    def setUp(self):
        self.tested = LineBotApi('channel_secret')

        self.rich_menu_id = 'richmenu-0000000000'
        self.user_id = 'userid'
        self.rich_menu = RichMenu(
            size=RichMenuSize(
                width=2500,
                height=1686
            ),
            selected=False,
            name="nice richmenu",
            chatBarText="touch me",
            areas=[
                RichMenuArea(
                    RichMenuBounds(
                        x=0,
                        y=0,
                        width=833,
                        height=843
                    ),
                    URITemplateAction(
                        uri='https://line.me/R/nv/location/'
                    )
                )
            ]
        )

    @responses.activate
    def test_get_rich_menu(self):
        responses.add(
            responses.GET,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/richmenu/rich_menu_id',
            json={
                "richMenuId": "rich_menu_id",
                "size": {
                    "width": 2500,
                    "height": 1686
                },
                "selected": False,
                "name": "name",
                "chatBarText": "chatBarText",
                "areas": [
                    {
                        "bounds": {
                            "x": 0,
                            "y": 0,
                            "width": 2500,
                            "height": 1686
                        },
                        "action": {
                            "type": "postback",
                            "data": "action=buy&itemid=123"
                        }
                    }
                ]
            },
            status=200
        )

        rich_menu = self.tested.get_rich_menu('rich_menu_id')

        request = responses.calls[0].request
        self.assertEqual(request.method, 'GET')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/richmenu/rich_menu_id'
        )

        self.assertEqual(rich_menu.rich_menu_id, 'rich_menu_id')
        self.assertEqual(rich_menu.size.width, 2500)
        self.assertEqual(rich_menu.size.height, 1686)
        self.assertEqual(rich_menu.selected, False)
        self.assertEqual(rich_menu.name, 'name')
        self.assertEqual(rich_menu.chat_bar_text, 'chatBarText')
        self.assertEqual(rich_menu.areas[0].bounds.x, 0)
        self.assertEqual(rich_menu.areas[0].bounds.y, 0)
        self.assertEqual(rich_menu.areas[0].bounds.width, 2500)
        self.assertEqual(rich_menu.areas[0].bounds.height, 1686)
        self.assertEqual(rich_menu.areas[0].action.type, 'postback')
        self.assertEqual(rich_menu.areas[0].action.data, 'action=buy&itemid=123')

    @responses.activate
    def test_create_rich_menu(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/richmenu',
            json={"richMenuId": "richMenuId"}, status=200
        )

        rich_menu = RichMenu(
            size=RichMenuSize(
                width=2500,
                height=1686
            ),
            selected=False,
            name="nice richmenu",
            chatBarText="touch me",
            areas=[
                RichMenuArea(
                    RichMenuBounds(
                        x=0,
                        y=0,
                        width=833,
                        height=843
                    ),
                    URITemplateAction(
                        uri='https://line.me/R/nv/location/'
                    )
                )
            ]
        )

        result = self.tested.create_rich_menu(rich_menu)

        request = responses.calls[0].request
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/richmenu'
        )
        self.assertEqual(result, "richMenuId")

    @responses.activate
    def test_delete_rich_menu(self):
        responses.add(
            responses.DELETE,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/richmenu/rich_menu_id',
            json={}, status=200
        )

        self.tested.delete_rich_menu('rich_menu_id')

        request = responses.calls[0].request
        self.assertEqual(request.method, 'DELETE')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/richmenu/rich_menu_id'
        )

    @responses.activate
    def test_get_rich_menu_id_of_user(self):
        responses.add(
            responses.GET,
            LineBotApi.DEFAULT_API_ENDPOINT +
            '/v2/bot/user/user_id/richmenu',
            json={"richMenuId": "richMenuId"}, status=200
        )

        result = self.tested.get_rich_menu_id_of_user('user_id')

        request = responses.calls[0].request
        self.assertEqual(request.method, 'GET')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/user/user_id/richmenu'
        )
        self.assertEqual(result, "richMenuId")

    @responses.activate
    def test_link_rich_menu_to_user(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT +
            '/v2/bot/user/user_id/richmenu/rich_menu_id',
            json={}, status=200
        )

        self.tested.link_rich_menu_to_user('user_id', 'rich_menu_id')

        request = responses.calls[0].request
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/user/user_id/richmenu/rich_menu_id'
        )

    @responses.activate
    def test_unlink_rich_menu_from_user(self):
        responses.add(
            responses.DELETE,
            LineBotApi.DEFAULT_API_ENDPOINT +
            '/v2/bot/user/user_id/richmenu',
            json={}, status=200
        )

        self.tested.unlink_rich_menu_from_user('user_id')

        request = responses.calls[0].request
        self.assertEqual(request.method, 'DELETE')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/user/user_id/richmenu'
        )

    @responses.activate
    def test_get_rich_menu_list(self):
        responses.add(
            responses.GET,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/richmenu/list',
            json={
                "richmenus": [
                    {
                        "richMenuId": "rich_menu_id",
                        "size": {
                            "width": 2500,
                            "height": 1686
                        },
                        "selected": False,
                        "name": "name",
                        "chatBarText": "chatBarText",
                        "areas": [
                            {
                                "bounds": {
                                    "x": 0,
                                    "y": 0,
                                    "width": 2500,
                                    "height": 1686
                                },
                                "action": {
                                    "type": "postback",
                                    "data": "action=buy&itemid=123"
                                }
                            }
                        ]
                    }
                ]
            },
            status=200
        )

        rich_menus = self.tested.get_rich_menu_list()

        request = responses.calls[0].request
        self.assertEqual(request.method, 'GET')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/richmenu/list'
        )
        self.assertEqual(rich_menus[0].rich_menu_id, 'rich_menu_id')
        self.assertEqual(rich_menus[0].size.width, 2500)
        self.assertEqual(rich_menus[0].size.height, 1686)
        self.assertEqual(rich_menus[0].selected, False)
        self.assertEqual(rich_menus[0].name, 'name')
        self.assertEqual(rich_menus[0].chat_bar_text, 'chatBarText')
        self.assertEqual(rich_menus[0].areas[0].bounds.x, 0)
        self.assertEqual(rich_menus[0].areas[0].bounds.y, 0)
        self.assertEqual(rich_menus[0].areas[0].bounds.width, 2500)
        self.assertEqual(rich_menus[0].areas[0].bounds.height, 1686)
        self.assertEqual(rich_menus[0].areas[0].action.type, 'postback')
        self.assertEqual(rich_menus[0].areas[0].action.data, 'action=buy&itemid=123')

    @responses.activate
    def test_link_rich_menu_to_users(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT +
            '/v2/bot/richmenu/bulk/link',
            json={}, status=202
        )

        self.tested.link_rich_menu_to_users(['user_id1', 'user_id2'], 'rich_menu_id')

        request = responses.calls[0].request
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/richmenu/bulk/link'
        )
        self.assertEqual(
            json.loads(request.body),
            {
                "richMenuId": "rich_menu_id",
                "userIds": ["user_id1", "user_id2"],
            }
        )

    @responses.activate
    def test_unlink_rich_menu_to_users(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT +
            '/v2/bot/richmenu/bulk/unlink',
            json={}, status=202
        )

        self.tested.unlink_rich_menu_from_users(['user_id1', 'user_id2'], 'rich_menu_id')

        request = responses.calls[0].request
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/richmenu/bulk/unlink'
        )
        self.assertEqual(
            json.loads(request.body),
            {
                "userIds": ["user_id1", "user_id2"],
            }
        )

    @responses.activate
    def test_set_default_rich_menu(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT +
            '/v2/bot/user/all/richmenu/rich_menu_id',
            json={}, status=200
        )

        self.tested.set_default_rich_menu('rich_menu_id')

        request = responses.calls[0].request
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/user/all/richmenu/rich_menu_id'
        )

    @responses.activate
    def test_get_default_rich_menu(self):
        responses.add(
            responses.GET,
            LineBotApi.DEFAULT_API_ENDPOINT +
            '/v2/bot/user/all/richmenu',
            json={"richMenuId": "richMenuId"}, status=200
        )

        result = self.tested.get_default_rich_menu()

        request = responses.calls[0].request
        self.assertEqual(request.method, 'GET')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/user/all/richmenu'
        )
        self.assertEqual(result, "richMenuId")

    @responses.activate
    def test_cancel_default_rich_menu(self):
        responses.add(
            responses.DELETE,
            LineBotApi.DEFAULT_API_ENDPOINT +
            '/v2/bot/user/all/richmenu',
            json={}, status=200
        )

        self.tested.cancel_default_rich_menu()

        request = responses.calls[0].request
        self.assertEqual(request.method, 'DELETE')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/user/all/richmenu'
        )

    @responses.activate
    def test_get_rich_menu_image(self):
        rich_menu_id = '1234'
        body = b'hogieoidksk'
        responses.add(
            responses.GET,
            LineBotApi.DEFAULT_API_DATA_ENDPOINT +
            '/v2/bot/richmenu/{rich_menu_id}/content'.format(rich_menu_id=rich_menu_id),
            body=body, status=200
        )

        res = self.tested.get_rich_menu_image(rich_menu_id)

        request = responses.calls[0].request
        self.assertEqual(request.method, 'GET')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_DATA_ENDPOINT +
            '/v2/bot/richmenu/{rich_menu_id}/content'.format(rich_menu_id=rich_menu_id),
        )
        self.assertEqual(
            body,
            res.content
        )

    @responses.activate
    def test_set_rich_menu_image(self):
        rich_menu_id = '1234'
        body = b'hogieoidksk'
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_DATA_ENDPOINT +
            '/v2/bot/richmenu/{rich_menu_id}/content'.format(rich_menu_id=rich_menu_id),
            json={}, status=200
        )

        self.tested.set_rich_menu_image(
            rich_menu_id=rich_menu_id,
            content_type='image/jpeg',
            content=body
        )

        request = responses.calls[0].request
        self.assertEqual('POST', request.method)
        self.assertEqual(
            LineBotApi.DEFAULT_API_DATA_ENDPOINT +
            '/v2/bot/richmenu/{rich_menu_id}/content'.format(rich_menu_id=rich_menu_id),
            request.url
        )

    @responses.activate
    def test_rich_menu_with_switch_action(self):
        rich_menu = RichMenu(
            size=RichMenuSize(
                width=2500,
                height=1686
            ),
            selected=False,
            name="nice richmenu",
            chatBarText="touch me",
            areas=[
                RichMenuArea(
                    RichMenuBounds(
                        x=0,
                        y=0,
                        width=833,
                        height=843
                    ),
                    RichMenuSwitchAction(
                        rich_menu_alias_id="richmenu-alias-a",
                        data="richmenu-changed-to-a"
                    )
                )
            ]
        )
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/richmenu',
            json={
                "richMenuId": "rich_menu_id",
                "size": {
                    "width": 2500,
                    "height": 1686
                },
                "selected": False,
                "name": "name",
                "chatBarText": "chatBarText",
                "areas": [
                    {
                        "bounds": {
                            "x": 0,
                            "y": 0,
                            "width": 2500,
                            "height": 1686
                        },
                        "action": {
                            "type": "richmenuswitch",
                            "richMenuAliasId": "richmenu-alias-a",
                            "data": "richmenu-changed-to-a"
                        }
                    }
                ]
            },
            status=200
        )

        result = self.tested.create_rich_menu(rich_menu)
        print(rich_menu)

        request = responses.calls[0].request
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/richmenu'
        )

        self.assertEqual(result, "rich_menu_id")
from aabb import TestLineBotApi()
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run()
#app.run(host='127.0.0.1', port=port)