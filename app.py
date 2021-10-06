from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


#======這裡是呼叫的檔案內容=====
from message import *
from new import *
from web_crawler import *
from config import *

from flask import Flask, request, abort, render_template
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
# from liffpy import LineFrontendFramework as LIFF, ErrorResponse
# from Function import *
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
import tempfile, os
import datetime
import time
#======python的函數庫==========
# liff_api = LIFF(CHANNEL_ACCESS_TOKEN)

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('HurLCRUu/4vC/xAgouIS5bzDPCEnF5yj9a5j7aQRm7GpgUowdNmAakAQ7GGXHunYXnQDeRg5HCbqEW5HuANq+Nd8gzkYZzUmkUWhVgvA7zAWJSJaEzCasR2e8yVNszuinqiz4KIMgzHyFsEuERuKQgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('918696c5608ab47deb783a6c0be85301')
user_id = "U9f266e60424eba94a01bbfa4f508fc28"

@app.route("/share_vedio")
def share_vedio():
    return render_template("./share_vedio.html")

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    print(body)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if '吃' in msg:
        message = quick_label()
        line_bot_api.reply_message(event.reply_token, message)
    elif "台式" in msg:
        message = Taiwan_Carousel()
        line_bot_api.reply_message(event.reply_token,message)
    # 隨機店家
    elif '隨機店家'in msg or "店家" in msg:
        message, menu_photo = Location_Message()
        line_bot_api.reply_message(event.reply_token, message)
        line_bot_api.push_message(user_id, menu_photo)
        # push_message 一個menu
    # 隨便
    elif "隨便" in msg or "都行" in msg:
        message = Random_food()
        line_bot_api.reply_message(event.reply_token, message)
    # elif msg.split("/", 1)[0] == "YT" or "yt":
    #     keyword = msg.split("/", 1)[1]
    #     message = youtube_vedio_parser(keyword)
    #     line_bot_api.reply_message(event.reply_token, message)
    else:
        message = TextSendMessage(text=msg)
        line_bot_api.reply_message(event.reply_token, message)


@handler.add(PostbackEvent)
def handle_message(event):
    print(event.postback.data)

@handler.add(MemberJoinedEvent)
def welcome(event):
    uid = event.joined.members[0].user_id
    gid = event.source.group_id
    profile = line_bot_api.get_group_member_profile(gid, uid)
    name = profile.display_name
    message = TextSendMessage(text=f'{name}歡迎加入')
    line_bot_api.reply_message(event.reply_token, message)
        
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
