import logging

from aiogram import types
from googletrans import Translator
from aiogram.types import CallbackQuery
from keyboards.inline.subs import show_channels
from keyboards.inline.language import language
from utils.misc.subs import check_sub_channels
from .oxford_look_up import getDefinitions
from aiogram.dispatcher import FSMContext
from loader import dp, bot

translator = Translator()

@dp.message_handler()
async def send_message(message: types.Message):
    lang = translator.detect(message.text).lang
    is_subs = await check_sub_channels(message)
    if is_subs:
        if len(message.text.split())>=1:
            await message.answer(f"{translator.translate(message.text, dest='en').text}\n\n"
                                 f"👇 Javobni qaysi tilda olishni xoxlaysiz ?",reply_markup=language)
        else:
            await message.reply("Bunday so'z topilmadi.\nNo Such word Found")

    else:
        btn = await show_channels()
        context = f"Xurmatli <b>{message.from_user.full_name}</b> botni ishlatishdan oldin quyidagi kanallarga obuna bo'ling 👇"
        await message.answer(text=context,reply_markup=btn)

@dp.callback_query_handler(text="uzb")
async def text_uzb(call: CallbackQuery):
    try:
        await call.answer(cache_time=60)
        is_subs = await check_sub_channels(call)
        lang = translator.detect(call.message.text).lang
        if is_subs:
            if lang!="uz":
                await call.message.edit_text(f"{translator.translate(call.message.text, dest='uz').text}\n\n",
                                             reply_markup=language)
            else:
                await call.message.edit_text(f"{call.message.text}\n\n",
                                             reply_markup=language)
        else:
            btn = await show_channels()
            context = f"Xurmatli <b>{call.from_user.full_name}</b> botni ishlatishdan oldin quyidagi kanallarga obuna bo'ling 👇"
            await call.message.answer(text=context, reply_markup=btn)
    except Exception as er:
        pass


@dp.callback_query_handler(text="rus")
async def text_uzb(call: CallbackQuery):
    try:
        await call.answer(cache_time=60)
        is_subs = await check_sub_channels(call)
        if is_subs:
            await call.message.edit_text(f"{translator.translate(call.message.text, dest='ru').text}\n\n",
                                         reply_markup=language)
        else:
            btn = await show_channels()
            context = f"Xurmatli <b>{call.from_user.full_name}</b> botni ishlatishdan oldin quyidagi kanallarga obuna bo'ling 👇"
            await call.message.answer(text=context, reply_markup=btn)
    except Exception as er:
        pass

@dp.callback_query_handler(text="kr")
async def text_uzb(call: CallbackQuery):
    try:
        await call.answer(cache_time=60)
        is_subs = await check_sub_channels(call)
        if is_subs:
            await call.message.edit_text(f"{translator.translate(call.message.text, dest='ko').text}\n\n",
                                         reply_markup=language)
        else:
            btn = await show_channels()
            context = f"Xurmatli <b>{call.from_user.full_name}</b> botni ishlatishdan oldin quyidagi kanallarga obuna bo'ling 👇"
            await call.message.answer(text=context, reply_markup=btn)
    except Exception as er:
        pass

@dp.callback_query_handler(text="en")
async def text_uzb(call: CallbackQuery):
    try:
        await call.answer(cache_time=60)
        is_subs = await check_sub_channels(call)
        if is_subs:
            await call.message.edit_text(f"{translator.translate(call.message.text, dest='en').text}\n\n",
                                         reply_markup=language)
        else:
            btn = await show_channels()
            context = f"Xurmatli <b>{call.from_user.full_name}</b> botni ishlatishdan oldin quyidagi kanallarga obuna bo'ling 👇"
            await call.message.answer(text=context, reply_markup=btn)
    except Exception as er:
        pass