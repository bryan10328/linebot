from functools import cache
from turtle import textinput
from flask import Flask, request, abort
import re
import os
import json
import requests
import menu_body
import client
import time
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,PostbackTemplateAction,CarouselColumn,URITemplateAction,CarouselTemplate
)

from linebot.models import ConfirmTemplate,PostbackAction,URIAction, MessageAction,FlexSendMessage, MessageTemplateAction,TemplateSendMessage, ButtonsTemplate,ImageCarouselTemplate,ImageCarouselColumn
app = Flask(__name__)

Users=[]
line_bot_api = LineBotApi('fJePXX8LsMpyKuVtiEJEFqc9u5HHDQwARHXVOwd4pbubcvnbJIADHPJwHH05zRQu6VwKd8UjyqMaGtTnltgxGfkgXqMmxS/RarrZrm4r1u1tVTz5YjueUGiIe5nTNZKcnW3+9E1/KYepnruMhmiZSwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('150c61e0afd1f4eae2e348a448f53b59')
 
headers = {"Authorization":"Bearer fJePXX8LsMpyKuVtiEJEFqc9u5HHDQwARHXVOwd4pbubcvnbJIADHPJwHH05zRQu6VwKd8UjyqMaGtTnltgxGfkgXqMmxS/RarrZrm4r1u1tVTz5YjueUGiIe5nTNZKcnW3+9E1/KYepnruMhmiZSwdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}
menuid=["","","","","","","","","","",""]
orderckeck=["奇異果","葡萄汁","蔓越莓","藍莓","百香果","洛神花茶","玫瑰花茶","蘋果茶","水果茶","花茶","抹茶拿鐵","青心烏龍","檸檬紅茶","普洱","茉香綠茶","天使之淚","末日黃昏","蘋紛秋色","莓飛色舞","浪漫紫幻","美式","拿鐵","濃縮","奶茶","綠奶","阿薩姆","烏龍奶茶","芋香奶茶","可可奶茶"]
def createmenu():
    #menuid[0]=menu_body.og( "og","og",["果汁","花果茶","茶飲","氣泡飲"],"wp_18_7_32_sp_05.jpg")
    #menuid[10]='richmenu-8f901df347c0a6c4124762cd4681649b'
    # menu_body.final( "final","送出",["繼續下單","完成送出"],"finally001.jpg")
# richmenu-1f8ee63494cb77f8bda9bd3a434ecad6
# richmenu-d657d2484c9e69b67a67d87057b6cb7f
# richmenu-9b0b77c41920b3a677d05943da298fbf
# richmenu-31d2f75c04866d86e7547755d366e461
# richmenu-93aae88750e93f504955725814af0817
# richmenu-c1bb2f65ed3cbb060f1637405e0e7ac8
# richmenu-2f2aa6950a73df34f46f065f1aa9d455
# richmenu-b8e41a9d15f3b4ac73b93e0e0822b2c0
# richmenu-fc48c290e5fbd90b26fd01c2d68aa48e
    #menuid[0]=menu_body.menu3x2( "menu","類別",["果汁","花果茶","茶飲","氣泡飲","咖啡","奶茶"],"b2.jpg")
    # menuid[1]=menu_body.menu3x2("juice","果汁",["奇異果","葡萄汁","蔓越莓","藍莓","百香果","menu"],"juice001.jpg")
    # menuid[2]=menu_body.menu3x2("scentedtea","花果茶",["洛神花茶","玫瑰花茶","蘋果茶","水果茶","花茶","menu"],"scentedtea001.jpg")
    # menuid[3]=menu_body.menu3x2("tea","茶飲",["抹茶拿鐵","青心烏龍","檸檬紅茶","普洱","茉香綠茶","menu"],"tea001.jpg")
    # menuid[4]=menu_body.menu3x2("sparkling","氣泡飲",["天使之淚","末日黃昏","蘋紛秋色","莓飛色舞","浪漫紫幻","menu"],"sparkling001.jpg")
    # menuid[5]=menu_body.menu4x1("coffee","咖啡",["美式","拿鐵","濃縮","menu"],"coffee001.jpg")
    # menuid[6]=menu_body.menu3x2("milktea","奶茶",["綠奶","阿薩姆","烏龍奶茶","芋香奶茶","可可奶茶","menu"],"milktea001.jpg")
    # menuid[7]=menu_body.size("size","SIZE",["上一頁","小","中","大"],"size001.jpg")
    # menuid[8]=menu_body.count("count","數量",["上一頁","-1","+1","確定"],"count001.jpg")
    # menuid[0]='richmenu-b8e41a9d15f3b4ac73b93e0e0822b2c0'
    # menuid[1]='richmenu-d657d2484c9e69b67a67d87057b6cb7f'
    # menuid[2]='richmenu-9b0b77c41920b3a677d05943da298fbf'
    # menuid[3]='richmenu-31d2f75c04866d86e7547755d366e461'
    # menuid[4]='richmenu-93aae88750e93f504955725814af0817'
    # menuid[5]='richmenu-c1bb2f65ed3cbb060f1637405e0e7ac8'
    # menuid[6]='richmenu-2f2aa6950a73df34f46f065f1aa9d455'
    # menuid[7]='richmenu-b8e41a9d15f3b4ac73b93e0e0822b2c0'
    # menuid[8]='richmenu-fc48c290e5fbd90b26fd01c2d68aa48e'
    # menuid[9]='richmenu-8f901df347c0a6c4124762cd4681649b'
    a=0

createmenu(); 
#line_bot_api.set_default_rich_menu(menuid[2])
rich_menu_list = line_bot_api.get_rich_menu_list()
print(len(rich_menu_list))
#line_bot_api.delete_rich_menu(rich_menu_list[1].rich_menu_id)

for rich_menu in rich_menu_list:
    print(rich_menu.chat_bar_text)
    try:
        check=False
        for ii in range(1,len(menuid)):
            if(rich_menu.rich_menu_id==menuid[ii]):
                check=True
        check=False
        if(check==False):
            print ("delete "+rich_menu.rich_menu_id)
            line_bot_api.delete_rich_menu(rich_menu.rich_menu_id)
            time.sleep(30)
       # line_bot_api.delete_rich_menu()
        
    except Exception as e:
        a=0
        print(str(e))
 

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
    switch(event.message.text,line_id,event.reply_token,profile)
    print(line_id)
 
def switch(text,userid,reply_token,profile):
        index=checkuser(profile)
        match text:
            case '果汁':
                Users[index].lastpos=text
                line_bot_api.link_rich_menu_to_user(userid,menuid[1])
                return text
            case '花果茶':
                Users[index].lastpos=text
                line_bot_api.link_rich_menu_to_user(userid,menuid[2])
                return text
            case '茶飲':
                Users[index].lastpos=text
                line_bot_api.link_rich_menu_to_user(userid,menuid[3])
                return text
            case '氣泡飲':
                Users[index].lastpos=text
                line_bot_api.link_rich_menu_to_user(userid,menuid[4])
                return text
            case '咖啡':
                Users[index].lastpos=text
                line_bot_api.link_rich_menu_to_user(userid,menuid[5])
                return text
            case '奶茶':
                Users[index].lastpos=text
                line_bot_api.link_rich_menu_to_user(userid,menuid[6])
                return text
            case 'menu':
                line_bot_api.link_rich_menu_to_user(userid,menuid[0])
                return text
            case '-1':
                if Users[index].tmpproduct=="" or Users[index].tmpsize=="" :
                    line_bot_api.link_rich_menu_to_user(userid,menuid[0])
                    return text
                else:
                    checkorder(reply_token,index,Users[index].tmpproduct,Users[index].tmpsize,-1)
                return text
            case '+1':
                if Users[index].tmpproduct=="" or Users[index].tmpsize=="" :
                    line_bot_api.link_rich_menu_to_user(userid,menuid[0])
                    return text
                else:
                    checkorder(reply_token,index,Users[index].tmpproduct,Users[index].tmpsize,+1)
              
                return text
            case '上一頁':
                try:
                    if Users[index].lastpos=="" :
                        line_bot_api.link_rich_menu_to_user(userid,menuid[0])
                        return text
                    if Users[index].lastpos2!="" :
                        checkreturn(Users[index].id,Users[index].lastpos2)
                        Users[index].lastpos2=""
                        return text
                    else:
                        checkreturn(Users[index].id,Users[index].lastpos)
                        return text
                except:
                    line_bot_api.link_rich_menu_to_user(userid,menuid[0])
            case '確定':
                finallyorder(reply_token,index,False)
                return
            case '繼續下單':
                line_bot_api.link_rich_menu_to_user(userid,menuid[0])
                return
            case '完成送出':
                finallyorder(reply_token,index,True)
                Users[index].orders=[]
                Users[index].tmpsize=""
                Users[index].lastpos=""
                Users[index].lastpos2=""
                Users[index].tmpproduct=""
                line_bot_api.link_rich_menu_to_user(userid,menuid[0])
                return



 
        for i in range(0,len(orderckeck)):
            if orderckeck[i]==text:
                Users[index].tmpsize=text
                Users[index].tmpproduct=text

                line_bot_api.link_rich_menu_to_user(userid,menuid[7])
                return text
        if text=="大" or  text=="中" or  text=="小":
            
            Users[index].lastpos2="size"
            Users[index].tmpsize=text
            checkorder(reply_token,index,Users[index].tmpproduct,text,0)
            line_bot_api.link_rich_menu_to_user(userid,menuid[8])
            return text



def checkuser(profile):
    for i in range(0,len(Users)):
        if Users[i].id==profile.user_id:
            return i
    oneuser=client.information()
 
    oneuser.id=profile.user_id
    oneuser.name=profile.display_name
    oneuser.pic=profile.picture_url

    Users.append(oneuser)
    return len(Users)-1
def checkorder(reply_token,index,product,size,count):
    getindex=-1
    for i in range(0,len(Users[index].orders)):
        if(Users[index].orders[i].product==product and Users[index].orders[i].size==size):
            getindex=i
    if getindex<0:        
        oneproduct=client.order()
        oneproduct.product=product
        oneproduct.size=size
        oneproduct.count=1
        Users[index].orders.append(oneproduct)
        getindex=len(Users[index].orders)-1
 
 
    Users[index].orders[getindex].count+=count
    zero=""
    if Users[index].orders[getindex].count<0:
        Users[index].orders[getindex].count=0
        
    messagesdata=Users[index].tmpproduct+" ["+Users[index].tmpsize+ "] 數量:"+str(Users[index].orders[getindex].count)
    if Users[index].orders[getindex].count==0:
        messagesdata+='\r'+"(數量0 表示取消"+Users[index].tmpproduct+"訂單)"
    messages = [TextSendMessage(text=messagesdata)]
    
    line_bot_api.reply_message(reply_token, messages)
    return
    # line_bot_api.reply_message(
    #         reply_token, TextSendMessage(text=Users[index].tmpproduct+" "+Users[index].tmpsize)+ "數量:"+oneproduct.count)
    
def finallyorder(reply_token,index,final):
    messagesdata=""
    if final:
        messagesdata="親愛的"+Users[index].name+'\r'+"  您的訂單有..."+'\r'        
    else:        
        messagesdata="目前訂單"+'\r'
    for  od in range(0,len(Users[index].orders)):
        if Users[index].orders[od].count>0:
            messagesdata+=Users[index].orders[od].product+" ["+Users[index].orders[od].size+"] 數量:"+str(Users[index].orders[od].count)
            if od<+len(Users[index].orders)-1:messagesdata+='\r'
        if messagesdata=="":messagesdata="沒有訂單" 
    messages = [TextSendMessage(text= messagesdata)]
   
    line_bot_api.reply_message(reply_token, messages)
    line_bot_api.link_rich_menu_to_user(Users[index].id,menuid[9])
    return
 

def checkreturn(userid,lastpost):
    match lastpost:
        case '果汁':
            line_bot_api.link_rich_menu_to_user(userid,menuid[1])
            return
        case '花果茶':
            line_bot_api.link_rich_menu_to_user(userid,menuid[2])
            return
        case '茶飲':
            line_bot_api.link_rich_menu_to_user(userid,menuid[3])
            return
        case '氣泡飲':
            line_bot_api.link_rich_menu_to_user(userid,menuid[4])
            return
        case '咖啡':
            line_bot_api.link_rich_menu_to_user(userid,menuid[5])
            return
        case '奶茶':
            line_bot_api.link_rich_menu_to_user(userid,menuid[6])
            return
        case 'size':
            line_bot_api.link_rich_menu_to_user(userid,menuid[7])
            return
 
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run()
#訂單 id name product[]