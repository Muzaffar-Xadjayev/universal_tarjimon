from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

language = InlineKeyboardMarkup(row_width=2)
uzb = InlineKeyboardButton(text="πΊπΏ O'zbek tili",callback_data="uzb")
rus = InlineKeyboardButton(text="π·πΊ Rus tili",callback_data="rus")
kr = InlineKeyboardButton(text="π°π· Koreys tili",callback_data="kr")
en = InlineKeyboardButton(text="πΊπΈ Ingliz tili", callback_data="en")
sa = InlineKeyboardButton(text="πΈπ¦ Arab tili", callback_data="ar")
jp = InlineKeyboardButton(text="π―π΅ Yapon tili", callback_data="ja")
language.add(uzb,rus,kr,en,sa,jp)