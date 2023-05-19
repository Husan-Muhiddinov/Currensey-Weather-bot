from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from .models import *

def home_markup():
    reply_markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    reply_markup.add(*[
        '☀️ Ob-havo',
        '💲 Valyutalar',
    ])
    return reply_markup


def region_markup():
    reply_markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    reply_markup.add(*[
        'Toshkent',
        'Samarqand',
        'Qashqadaryo',
        "Farg'ona",
        'Andijon',
        'Namangan',
        'Sirdaryo',
        'Buxoro',
        'Jizzax',
        'Navoiy',
    ])
    reply_markup.add(*['🔙 Orqaga'])
    return reply_markup

def cost_markup():
    reply_markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    reply_markup.add(*[
        'Bank',
        'Qora bozor',
    ])
    reply_markup.add(*['🔙 Orqaga'])
    return reply_markup