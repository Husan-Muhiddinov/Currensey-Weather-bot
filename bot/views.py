import telebot
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from telebot import types
from .markups import *
import requests
import json

TOKEN="6263605675:AAHNsbW84ytmhgn4hD6uLhLqkPCGZp-HZag"
bot = telebot.TeleBot(TOKEN)
bot.remove_webhook()
bot.set_webhook(url='https://e8fc-195-158-2-216.ngrok-free.app')


@csrf_exempt
def index(request) :
    if request.method=="POST":
        update=telebot.types.Update.de_json(request.body.decode('utf-8'))
        bot.process_new_updates([update])
    return HttpResponse('<h1>Xush kelibsiz!</h1>')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(chat_id=message.chat.id, text=f"Assalomu alaykum <b>{message.from_user.first_name}</b>! botimizga xush kelibsiz", reply_markup=home_markup(), parse_mode="HTML")

@bot.message_handler(func=lambda m: True)
def echo_message(message):
    if message.text == '☀️ Ob-havo':
        bot.send_message(message.from_user.id, f"Qaysi viloyatning ob-havo ma'lumoti kerak tanlang!", reply_markup=region_markup())

    elif message.text == '💲 Valyutalar':
        bot.send_message(message.from_user.id, f"Valyutalar", reply_markup=cost_markup())
        
    elif message.text == '🔙 Orqaga':
            text = "Bosh sahifa:"
            bot.send_message(message.from_user.id, text, reply_markup=home_markup())

    elif message.text == "Toshkent":
        req=requests.get("http://api.weatherapi.com/v1/future.json?key=24c42d446e124408992134203231605&q=Tashkent&dt=2023-06-19")
        js_req=json.loads(req.text)
        a=js_req['forecast']['forecastday']
        for i in a:
            b=i['hour']
            list=[]
            list1=[]
            list2=[]
            for j in b:
                list.append(j['time'])
                list1.append(j['temp_c'])
                list2.append(j['wind_mph'])
        text=f"<b>{js_req['location']['name']}</b> viloyati uchun:\n\nsana: <b>{i['date']}</b>\n\nBugun havo harorati [<b>{i['day']['maxtemp_c']}°C ; {i['day']['mintemp_c']}°C</b>] oraliqda bo'lishi kutilmoqda!\n\n<b>{list[0]}</b> vaqtda\nHarorat:  <b>{list1[0]}°C</b>\nShamol tezligi:  <b>{list2[0]}km/s</b>\n\n<b>{list[1]}</b> vaqtda\nHarorat:  <b>{list1[1]}°C</b>\nShamol tezligi:  <b>{list2[1]}km/s</b>\n\n<b>{list[2]}</b> vaqtda\nHarorat:  <b>{list1[2]}°C</b>\nShamol tezligi:  <b>{list2[2]}km/s</b>\n\n<b>{list[3]}</b> vaqtda\nHarorat:  <b>{list1[3]}°C</b>\nShamol tezligi:  <b>{list2[3]}km/s</b>\n\n<b>{list[4]}</b> vaqtda\nHarorat:  <b>{list1[4]}°C</b>\nShamol tezligi:  <b>{list2[4]}km/s</b>\n\n<b>{list[5]}</b> vaqtda\nHarorat:  <b>{list1[5]}°C</b>\nShamol tezligi:  <b>{list2[5]}km/s</b>\n\n<b>{list[6]}</b> vaqtda\nHarorat:  <b>{list1[6]}°C</b>\nShamol tezligi:  <b>{list2[6]}km/s</b>\n\n<b>{list[7]}</b> vaqtda\nHarorat:  <b>{list1[7]}°C</b>\nShamol tezligi:  <b>{list2[7]}km/s</b>"
        bot.send_message(message.from_user.id, text, parse_mode="HTML")

    elif message.text == "Qashqadaryo":
        req=requests.get("http://api.weatherapi.com/v1/future.json?key=24c42d446e124408992134203231605&q=Kashkadarya&dt=2023-06-19")
        js_req=json.loads(req.text)
        a=js_req['forecast']['forecastday']
        for i in a:
            b=i['hour']
            list=[]
            list1=[]
            list2=[]
            for j in b:
                list.append(j['time'])
                list1.append(j['temp_c'])
                list2.append(j['wind_mph'])
        text=f"<b>{js_req['location']['name']}</b> viloyati uchun:\n\nsana: <b>{i['date']}</b>\n\nBugun havo harorati [<b>{i['day']['maxtemp_c']}°C ; {i['day']['mintemp_c']}°C</b>] oraliqda bo'lishi kutilmoqda!\n\n<b>{list[0]}</b> vaqtda\nHarorat:  <b>{list1[0]}°C</b>\nShamol tezligi:  <b>{list2[0]}km/s</b>\n\n<b>{list[1]}</b> vaqtda\nHarorat:  <b>{list1[1]}°C</b>\nShamol tezligi:  <b>{list2[1]}km/s</b>\n\n<b>{list[2]}</b> vaqtda\nHarorat:  <b>{list1[2]}°C</b>\nShamol tezligi:  <b>{list2[2]}km/s</b>\n\n<b>{list[3]}</b> vaqtda\nHarorat:  <b>{list1[3]}°C</b>\nShamol tezligi:  <b>{list2[3]}km/s</b>\n\n<b>{list[4]}</b> vaqtda\nHarorat:  <b>{list1[4]}°C</b>\nShamol tezligi:  <b>{list2[4]}km/s</b>\n\n<b>{list[5]}</b> vaqtda\nHarorat:  <b>{list1[5]}°C</b>\nShamol tezligi:  <b>{list2[5]}km/s</b>\n\n<b>{list[6]}</b> vaqtda\nHarorat:  <b>{list1[6]}°C</b>\nShamol tezligi:  <b>{list2[6]}km/s</b>\n\n<b>{list[7]}</b> vaqtda\nHarorat:  <b>{list1[7]}°C</b>\nShamol tezligi:  <b>{list2[7]}km/s</b>"
        bot.send_message(message.from_user.id, text, parse_mode="HTML")

    elif message.text == "Samarqand":
        req=requests.get("http://api.weatherapi.com/v1/future.json?key=24c42d446e124408992134203231605&q=Samarkand&dt=2023-06-19")
        js_req=json.loads(req.text)
        a=js_req['forecast']['forecastday']
        for i in a:
            b=i['hour']
            list=[]
            list1=[]
            list2=[]
            for j in b:
                list.append(j['time'])
                list1.append(j['temp_c'])
                list2.append(j['wind_mph'])
        text=f"<b>{js_req['location']['name']}</b> viloyati uchun:\n\nsana: <b>{i['date']}</b>\n\nBugun havo harorati [<b>{i['day']['maxtemp_c']}°C ; {i['day']['mintemp_c']}°C</b>] oraliqda bo'lishi kutilmoqda!\n\n<b>{list[0]}</b> vaqtda\nHarorat:  <b>{list1[0]}°C</b>\nShamol tezligi:  <b>{list2[0]}km/s</b>\n\n<b>{list[1]}</b> vaqtda\nHarorat:  <b>{list1[1]}°C</b>\nShamol tezligi:  <b>{list2[1]}km/s</b>\n\n<b>{list[2]}</b> vaqtda\nHarorat:  <b>{list1[2]}°C</b>\nShamol tezligi:  <b>{list2[2]}km/s</b>\n\n<b>{list[3]}</b> vaqtda\nHarorat:  <b>{list1[3]}°C</b>\nShamol tezligi:  <b>{list2[3]}km/s</b>\n\n<b>{list[4]}</b> vaqtda\nHarorat:  <b>{list1[4]}°C</b>\nShamol tezligi:  <b>{list2[4]}km/s</b>\n\n<b>{list[5]}</b> vaqtda\nHarorat:  <b>{list1[5]}°C</b>\nShamol tezligi:  <b>{list2[5]}km/s</b>\n\n<b>{list[6]}</b> vaqtda\nHarorat:  <b>{list1[6]}°C</b>\nShamol tezligi:  <b>{list2[6]}km/s</b>\n\n<b>{list[7]}</b> vaqtda\nHarorat:  <b>{list1[7]}°C</b>\nShamol tezligi:  <b>{list2[7]}km/s</b>"
        bot.send_message(message.from_user.id, text, parse_mode="HTML")

    elif message.text == "Farg'ona":
        req=requests.get("http://api.weatherapi.com/v1/future.json?key=24c42d446e124408992134203231605&q=Fergana&dt=2023-06-19")
        js_req=json.loads(req.text)
        a=js_req['forecast']['forecastday']
        for i in a:
            b=i['hour']
            list=[]
            list1=[]
            list2=[]
            for j in b:
                list.append(j['time'])
                list1.append(j['temp_c'])
                list2.append(j['wind_mph'])
        text=f"<b>{js_req['location']['name']}</b> viloyati uchun:\n\nsana: <b>{i['date']}</b>\n\nBugun havo harorati [<b>{i['day']['maxtemp_c']}°C ; {i['day']['mintemp_c']}°C</b>] oraliqda bo'lishi kutilmoqda!\n\n<b>{list[0]}</b> vaqtda\nHarorat:  <b>{list1[0]}°C</b>\nShamol tezligi:  <b>{list2[0]}km/s</b>\n\n<b>{list[1]}</b> vaqtda\nHarorat:  <b>{list1[1]}°C</b>\nShamol tezligi:  <b>{list2[1]}km/s</b>\n\n<b>{list[2]}</b> vaqtda\nHarorat:  <b>{list1[2]}°C</b>\nShamol tezligi:  <b>{list2[2]}km/s</b>\n\n<b>{list[3]}</b> vaqtda\nHarorat:  <b>{list1[3]}°C</b>\nShamol tezligi:  <b>{list2[3]}km/s</b>\n\n<b>{list[4]}</b> vaqtda\nHarorat:  <b>{list1[4]}°C</b>\nShamol tezligi:  <b>{list2[4]}km/s</b>\n\n<b>{list[5]}</b> vaqtda\nHarorat:  <b>{list1[5]}°C</b>\nShamol tezligi:  <b>{list2[5]}km/s</b>\n\n<b>{list[6]}</b> vaqtda\nHarorat:  <b>{list1[6]}°C</b>\nShamol tezligi:  <b>{list2[6]}km/s</b>\n\n<b>{list[7]}</b> vaqtda\nHarorat:  <b>{list1[7]}°C</b>\nShamol tezligi:  <b>{list2[7]}km/s</b>"
        bot.send_message(message.from_user.id, text, parse_mode="HTML")

    elif message.text == "Andijon":
        req=requests.get("http://api.weatherapi.com/v1/future.json?key=24c42d446e124408992134203231605&q=Andijan&dt=2023-06-19")
        js_req=json.loads(req.text)
        a=js_req['forecast']['forecastday']
        for i in a:
            b=i['hour']
            list=[]
            list1=[]
            list2=[]
            for j in b:
                list.append(j['time'])
                list1.append(j['temp_c'])
                list2.append(j['wind_mph'])
        text=f"<b>{js_req['location']['name']}</b> viloyati uchun:\n\nsana: <b>{i['date']}</b>\n\nBugun havo harorati [<b>{i['day']['maxtemp_c']}°C ; {i['day']['mintemp_c']}°C</b>] oraliqda bo'lishi kutilmoqda!\n\n<b>{list[0]}</b> vaqtda\nHarorat:  <b>{list1[0]}°C</b>\nShamol tezligi:  <b>{list2[0]}km/s</b>\n\n<b>{list[1]}</b> vaqtda\nHarorat:  <b>{list1[1]}°C</b>\nShamol tezligi:  <b>{list2[1]}km/s</b>\n\n<b>{list[2]}</b> vaqtda\nHarorat:  <b>{list1[2]}°C</b>\nShamol tezligi:  <b>{list2[2]}km/s</b>\n\n<b>{list[3]}</b> vaqtda\nHarorat:  <b>{list1[3]}°C</b>\nShamol tezligi:  <b>{list2[3]}km/s</b>\n\n<b>{list[4]}</b> vaqtda\nHarorat:  <b>{list1[4]}°C</b>\nShamol tezligi:  <b>{list2[4]}km/s</b>\n\n<b>{list[5]}</b> vaqtda\nHarorat:  <b>{list1[5]}°C</b>\nShamol tezligi:  <b>{list2[5]}km/s</b>\n\n<b>{list[6]}</b> vaqtda\nHarorat:  <b>{list1[6]}°C</b>\nShamol tezligi:  <b>{list2[6]}km/s</b>\n\n<b>{list[7]}</b> vaqtda\nHarorat:  <b>{list1[7]}°C</b>\nShamol tezligi:  <b>{list2[7]}km/s</b>"
        bot.send_message(message.from_user.id, text, parse_mode="HTML")

    elif message.text == "Namangan":
        req=requests.get("http://api.weatherapi.com/v1/future.json?key=24c42d446e124408992134203231605&q=Namangan&dt=2023-06-19")
        js_req=json.loads(req.text)
        a=js_req['forecast']['forecastday']
        for i in a:
            b=i['hour']
            list=[]
            list1=[]
            list2=[]
            for j in b:
                list.append(j['time'])
                list1.append(j['temp_c'])
                list2.append(j['wind_mph'])
        text=f"<b>{js_req['location']['name']}</b> viloyati uchun:\n\nsana: <b>{i['date']}</b>\n\nBugun havo harorati [<b>{i['day']['maxtemp_c']}°C ; {i['day']['mintemp_c']}°C</b>] oraliqda bo'lishi kutilmoqda!\n\n<b>{list[0]}</b> vaqtda\nHarorat:  <b>{list1[0]}°C</b>\nShamol tezligi:  <b>{list2[0]}km/s</b>\n\n<b>{list[1]}</b> vaqtda\nHarorat:  <b>{list1[1]}°C</b>\nShamol tezligi:  <b>{list2[1]}km/s</b>\n\n<b>{list[2]}</b> vaqtda\nHarorat:  <b>{list1[2]}°C</b>\nShamol tezligi:  <b>{list2[2]}km/s</b>\n\n<b>{list[3]}</b> vaqtda\nHarorat:  <b>{list1[3]}°C</b>\nShamol tezligi:  <b>{list2[3]}km/s</b>\n\n<b>{list[4]}</b> vaqtda\nHarorat:  <b>{list1[4]}°C</b>\nShamol tezligi:  <b>{list2[4]}km/s</b>\n\n<b>{list[5]}</b> vaqtda\nHarorat:  <b>{list1[5]}°C</b>\nShamol tezligi:  <b>{list2[5]}km/s</b>\n\n<b>{list[6]}</b> vaqtda\nHarorat:  <b>{list1[6]}°C</b>\nShamol tezligi:  <b>{list2[6]}km/s</b>\n\n<b>{list[7]}</b> vaqtda\nHarorat:  <b>{list1[7]}°C</b>\nShamol tezligi:  <b>{list2[7]}km/s</b>"
        bot.send_message(message.from_user.id, text, parse_mode="HTML")

    elif message.text == "Sirdaryo":
        req=requests.get("http://api.weatherapi.com/v1/future.json?key=24c42d446e124408992134203231605&q=SyrDarya&dt=2023-06-19")
        js_req=json.loads(req.text)
        a=js_req['forecast']['forecastday']
        for i in a:
            b=i['hour']
            list=[]
            list1=[]
            list2=[]
            for j in b:
                list.append(j['time'])
                list1.append(j['temp_c'])
                list2.append(j['wind_mph'])
        text=f"<b>{js_req['location']['name']}</b> viloyati uchun:\n\nsana: <b>{i['date']}</b>\n\nBugun havo harorati [<b>{i['day']['maxtemp_c']}°C ; {i['day']['mintemp_c']}°C</b>] oraliqda bo'lishi kutilmoqda!\n\n<b>{list[0]}</b> vaqtda\nHarorat:  <b>{list1[0]}°C</b>\nShamol tezligi:  <b>{list2[0]}km/s</b>\n\n<b>{list[1]}</b> vaqtda\nHarorat:  <b>{list1[1]}°C</b>\nShamol tezligi:  <b>{list2[1]}km/s</b>\n\n<b>{list[2]}</b> vaqtda\nHarorat:  <b>{list1[2]}°C</b>\nShamol tezligi:  <b>{list2[2]}km/s</b>\n\n<b>{list[3]}</b> vaqtda\nHarorat:  <b>{list1[3]}°C</b>\nShamol tezligi:  <b>{list2[3]}km/s</b>\n\n<b>{list[4]}</b> vaqtda\nHarorat:  <b>{list1[4]}°C</b>\nShamol tezligi:  <b>{list2[4]}km/s</b>\n\n<b>{list[5]}</b> vaqtda\nHarorat:  <b>{list1[5]}°C</b>\nShamol tezligi:  <b>{list2[5]}km/s</b>\n\n<b>{list[6]}</b> vaqtda\nHarorat:  <b>{list1[6]}°C</b>\nShamol tezligi:  <b>{list2[6]}km/s</b>\n\n<b>{list[7]}</b> vaqtda\nHarorat:  <b>{list1[7]}°C</b>\nShamol tezligi:  <b>{list2[7]}km/s</b>"
        bot.send_message(message.from_user.id, text, parse_mode="HTML")

    elif message.text == "Buxoro":
        req=requests.get("http://api.weatherapi.com/v1/future.json?key=24c42d446e124408992134203231605&q=Bukhara&dt=2023-06-19")
        js_req=json.loads(req.text)
        a=js_req['forecast']['forecastday']
        for i in a:
            b=i['hour']
            list=[]
            list1=[]
            list2=[]
            for j in b:
                list.append(j['time'])
                list1.append(j['temp_c'])
                list2.append(j['wind_mph'])
        text=f"<b>{js_req['location']['name']}</b> viloyati uchun:\n\nsana: <b>{i['date']}</b>\n\nBugun havo harorati [<b>{i['day']['maxtemp_c']}°C ; {i['day']['mintemp_c']}°C</b>] oraliqda bo'lishi kutilmoqda!\n\n<b>{list[0]}</b> vaqtda\nHarorat:  <b>{list1[0]}°C</b>\nShamol tezligi:  <b>{list2[0]}km/s</b>\n\n<b>{list[1]}</b> vaqtda\nHarorat:  <b>{list1[1]}°C</b>\nShamol tezligi:  <b>{list2[1]}km/s</b>\n\n<b>{list[2]}</b> vaqtda\nHarorat:  <b>{list1[2]}°C</b>\nShamol tezligi:  <b>{list2[2]}km/s</b>\n\n<b>{list[3]}</b> vaqtda\nHarorat:  <b>{list1[3]}°C</b>\nShamol tezligi:  <b>{list2[3]}km/s</b>\n\n<b>{list[4]}</b> vaqtda\nHarorat:  <b>{list1[4]}°C</b>\nShamol tezligi:  <b>{list2[4]}km/s</b>\n\n<b>{list[5]}</b> vaqtda\nHarorat:  <b>{list1[5]}°C</b>\nShamol tezligi:  <b>{list2[5]}km/s</b>\n\n<b>{list[6]}</b> vaqtda\nHarorat:  <b>{list1[6]}°C</b>\nShamol tezligi:  <b>{list2[6]}km/s</b>\n\n<b>{list[7]}</b> vaqtda\nHarorat:  <b>{list1[7]}°C</b>\nShamol tezligi:  <b>{list2[7]}km/s</b>"
        bot.send_message(message.from_user.id, text, parse_mode="HTML")

    elif message.text == "Jizzax":
        req=requests.get("http://api.weatherapi.com/v1/future.json?key=24c42d446e124408992134203231605&q=Jizzakh&dt=2023-06-19")
        js_req=json.loads(req.text)
        a=js_req['forecast']['forecastday']
        for i in a:
            b=i['hour']
            list=[]
            list1=[]
            list2=[]
            for j in b:
                list.append(j['time'])
                list1.append(j['temp_c'])
                list2.append(j['wind_mph'])
        text=f"<b>{js_req['location']['name']}</b> viloyati uchun:\n\nsana: <b>{i['date']}</b>\n\nBugun havo harorati [<b>{i['day']['maxtemp_c']}°C ; {i['day']['mintemp_c']}°C</b>] oraliqda bo'lishi kutilmoqda!\n\n<b>{list[0]}</b> vaqtda\nHarorat:  <b>{list1[0]}°C</b>\nShamol tezligi:  <b>{list2[0]}km/s</b>\n\n<b>{list[1]}</b> vaqtda\nHarorat:  <b>{list1[1]}°C</b>\nShamol tezligi:  <b>{list2[1]}km/s</b>\n\n<b>{list[2]}</b> vaqtda\nHarorat:  <b>{list1[2]}°C</b>\nShamol tezligi:  <b>{list2[2]}km/s</b>\n\n<b>{list[3]}</b> vaqtda\nHarorat:  <b>{list1[3]}°C</b>\nShamol tezligi:  <b>{list2[3]}km/s</b>\n\n<b>{list[4]}</b> vaqtda\nHarorat:  <b>{list1[4]}°C</b>\nShamol tezligi:  <b>{list2[4]}km/s</b>\n\n<b>{list[5]}</b> vaqtda\nHarorat:  <b>{list1[5]}°C</b>\nShamol tezligi:  <b>{list2[5]}km/s</b>\n\n<b>{list[6]}</b> vaqtda\nHarorat:  <b>{list1[6]}°C</b>\nShamol tezligi:  <b>{list2[6]}km/s</b>\n\n<b>{list[7]}</b> vaqtda\nHarorat:  <b>{list1[7]}°C</b>\nShamol tezligi:  <b>{list2[7]}km/s</b>"
        bot.send_message(message.from_user.id, text, parse_mode="HTML")

    elif message.text == "Navoiy":
        req=requests.get("http://api.weatherapi.com/v1/future.json?key=24c42d446e124408992134203231605&q=Navoi&dt=2023-06-19")
        js_req=json.loads(req.text)
        a=js_req['forecast']['forecastday']
        for i in a:
            b=i['hour']
            list=[]
            list1=[]
            list2=[]
            for j in b:
                list.append(j['time'])
                list1.append(j['temp_c'])
                list2.append(j['wind_mph'])
        text=f"<b>{js_req['location']['name']}</b> viloyati uchun:\n\nsana: <b>{i['date']}</b>\n\nBugun havo harorati [<b>{i['day']['maxtemp_c']}°C ; {i['day']['mintemp_c']}°C</b>] oraliqda bo'lishi kutilmoqda!\n\n<b>{list[0]}</b> vaqtda\nHarorat:  <b>{list1[0]}°C</b>\nShamol tezligi:  <b>{list2[0]}km/s</b>\n\n<b>{list[1]}</b> vaqtda\nHarorat:  <b>{list1[1]}°C</b>\nShamol tezligi:  <b>{list2[1]}km/s</b>\n\n<b>{list[2]}</b> vaqtda\nHarorat:  <b>{list1[2]}°C</b>\nShamol tezligi:  <b>{list2[2]}km/s</b>\n\n<b>{list[3]}</b> vaqtda\nHarorat:  <b>{list1[3]}°C</b>\nShamol tezligi:  <b>{list2[3]}km/s</b>\n\n<b>{list[4]}</b> vaqtda\nHarorat:  <b>{list1[4]}°C</b>\nShamol tezligi:  <b>{list2[4]}km/s</b>\n\n<b>{list[5]}</b> vaqtda\nHarorat:  <b>{list1[5]}°C</b>\nShamol tezligi:  <b>{list2[5]}km/s</b>\n\n<b>{list[6]}</b> vaqtda\nHarorat:  <b>{list1[6]}°C</b>\nShamol tezligi:  <b>{list2[6]}km/s</b>\n\n<b>{list[7]}</b> vaqtda\nHarorat:  <b>{list1[7]}°C</b>\nShamol tezligi:  <b>{list2[7]}km/s</b>"
        bot.send_message(message.from_user.id, text, parse_mode="HTML")

    elif message.text == "Qora bozor":
            req=requests.get("https://nbu.uz/uz/exchange-rates/json/")
            js_req=json.loads(req.text)
            list=[]
            for i in js_req:
                list.append(i["nbu_cell_price"])
            reply = f"""1 USD = <b>{list[23]} so'm</b>\n1 EUR = <b>{list[7]} so'm</b>\n1 RUB = <b>{list[18]} so'm</b>\n"""
            bot.send_message(message.chat.id, reply, parse_mode="HTML")

    elif message.text == "Bank":
        req=requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/")
        js_req=json.loads(req.text)
        list=[]
        for i in js_req:
            list.append(i["Rate"])
        reply = f"""1 USD = <b>{list[0]} so'm</b>\n1 EUR = <b>{list[1]} so'm</b>\n1 RUB = <b>{list[2]} so'm</b>\n"""
        bot.send_message(message.chat.id, reply, parse_mode="HTML")



if __name__ == '__main__':
    bot.polling(none_stop=True)