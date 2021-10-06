#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
import json
from random import randint,sample


#TemplateSendMessage - ConfirmTemplate(確認介面訊息)
def Confirm_Template():
    message = TemplateSendMessage(
        alt_text='更多功能',
        template=ConfirmTemplate(
            text="更多功能",
            actions=[
                PostbackTemplateAction(
                    label="新增店家菜單",
                    text="新增店家菜單",
                ),
                MessageTemplateAction(
                    label="希望增加功能",
                    text="希望增加功能"
                )
            ]
        )
    )
    return message

#TemplateSendMessage - ImageCarouselTemplate(圖片旋轉木馬)
def image_carousel_message1():
    message = TemplateSendMessage(
        alt_text='圖片旋轉木馬',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/uKYgfVs.jpg",
                    action=URITemplateAction(
                        label="新鮮水果",
                        uri="http://img.juimg.com/tuku/yulantu/110709/222-110F91G31375.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/QOcAvjt.jpg",
                    action=URITemplateAction(
                        label="新鮮蔬菜",
                        uri="https://cdn.101mediaimage.com/img/file/1410464751urhp5.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/Np7eFyj.jpg",
                    action=URITemplateAction(
                        label="可愛狗狗",
                        uri="http://imgm.cnmo-img.com.cn/appimg/screenpic/big/674/673928.JPG"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/QRIa5Dz.jpg",
                    action=URITemplateAction(
                        label="可愛貓咪",
                        uri="https://m-miya.net/wp-content/uploads/2014/07/0-065-1.min_.jpg"
                    )
                )
            ]
        )


    )
    return message

#關於LINEBOT聊天內容範例
#異國餐廳
def quick_label():
    message = TextSendMessage(text='搜尋異國餐廳',
        quick_reply=QuickReply(items=[
            QuickReplyButton(action=MessageAction(label="台式", text="台式")),
            QuickReplyButton(action=MessageAction(label="美式", text="美式")),
            QuickReplyButton(action=MessageAction(label="泰式", text="泰式")),
            QuickReplyButton(action=MessageAction(label="韓式", text="韓式")),
            QuickReplyButton(action=MessageAction(label="義式", text="義式")),
            QuickReplyButton(action=MessageAction(label="港式", text="港式")),
            QuickReplyButton(image_url = "https://cdn-icons-png.flaticon.com/512/2346/2346242.png",action=MessageAction(label="日式", text="日式")),
            QuickReplyButton(action=MessageAction(label="法式", text="法式")),
            QuickReplyButton(action=MessageAction(label="其他", text="其他"))
            ]
        )
    )

    return message

with open('taiwan_randomfood.json') as file:
    taiwan_randomfood = json.load(file)
def Taiwan_Carousel():
    num = sample(range(0,len(taiwan_randomfood)),2)
    store_index1= num[0]
    store_index2 = num[1]

    food_list1 = list(taiwan_randomfood[store_index1]["food"].keys())
    price_list1 = list(taiwan_randomfood[store_index1]["food"].values())

    food_list2 = list(taiwan_randomfood[store_index2]["food"].keys())
    price_list2 = list(taiwan_randomfood[store_index2]["food"].values())

    food_index1 = randint(0,len(food_list1)-1)
    food1 = food_list1[food_index1]
    price1 = str(price_list1[food_index1])

    food_index2= randint(0,len(food_list2)-1)
    food2= food_list2[food_index2]
    price2 = str(price_list2[food_index2])

    store1 = taiwan_randomfood[store_index1]["store"]
    store2 = taiwan_randomfood[store_index2]["store"]

    menu1 = taiwan_randomfood[store_index1]["menu"]
    menu2 = taiwan_randomfood[store_index2]["menu"]

    message = TemplateSendMessage(
        alt_text='搜尋異國餐廳',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    # thumbnail_image_url='https://i.imgur.com/6gIiZ47.jpg',
                    title= food1 +" "+ price1 + "元",
                    text= store1,
                    actions=[
   
                        URITemplateAction(
                            label='菜單',
                            uri= menu1
                        )
                    ]
                ),
                CarouselColumn(
                    # thumbnail_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuo7n2_HNSFuT3T7Z9PUZmn1SDM6G6-iXfRC3FxdGTj7X1Wr0RzA',
                    title= food2 +" "+ price2 + "元",
                    text= store2,
                    actions=[
                        URITemplateAction(
                            label='菜單',
                            uri= menu2
                        )
                    ]
                ),
            ]
        )
    )
    return message
#隨機餐點
 
#隨機店家
with open('store.json') as file:
    data = json.load(file)

def Location_Message():
    index = randint(0,len(data)-1)
    store_name = str(data[index]["store"]) # "string"
    store_address = data[index]["address"]
    store_latitude = data[index]["latitude"]
    store_longitude = data[index]["longitude"]
    menu = data[index]["menu"]

    message = LocationSendMessage(
        title= store_name,
        address= store_address,
        latitude= store_latitude,
        longitude= store_longitude
    )

    menu_photo = ImageSendMessage(
        original_content_url= menu, 
        preview_image_url= menu
        )

    return message, menu_photo

with open('randomfood.json') as file:
    randomfood = json.load(file)
def Random_food():
    store_index =  randint(0,len(randomfood)-1)
    food_list = list(randomfood[store_index]["food"].keys())
    price_list = list(randomfood[store_index]["food"].values())

    food_index = randint(0,len(food_list)-1)

    food_name = food_list[food_index]
    food_price = str(price_list[food_index])
    store_name = randomfood[store_index]["store"]
    message  = TextSendMessage(
        text= food_name + " " + food_price+ "元" + "\n店名: " + store_name
    )
    return message