from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

language = InlineKeyboardMarkup(row_width=2)
uzb = InlineKeyboardButton(text="🇺🇿 O'zbek tili",callback_data="uzb")
rus = InlineKeyboardButton(text="🇷🇺 Rus tili",callback_data="rus")
kr = InlineKeyboardButton(text="🇰🇷 Koreys tili",callback_data="kr")
en = InlineKeyboardButton(text="🇺🇸 Ingliz tili", callback_data="en")
sa = InlineKeyboardButton(text="🇸🇦 Arab tili", callback_data="ar")
jp = InlineKeyboardButton(text="🇯🇵 Yapon tili", callback_data="ja")
language.add(uzb,rus,kr,en,sa,jp)