import asyncpg.exceptions
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import CHANNELS
from aiogram.types import CallbackQuery
from data.config import ADMINS
from keyboards.inline.subs import show_channels
from loader import dp, db, bot
from utils.misc.subs import check_sub_channels

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    is_subs = await check_sub_channels(message)
    if is_subs:
    # ADD USER IN DB
        try:
            await db.add_user(
                telegram_id=message.from_user.id,
                full_name=name,
                username=message.from_user.username
            )
            await message.answer(f"Assalomu alaykum, {message.from_user.full_name}!\n<b>Universal Tarjimon Botiga</b> xush kelibsiz!")
            await message.answer("Xabaringizni yuboring: ")
            count = await db.select_all_user()
            msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {len(count)} ta foydalanuvchi bor."
            try:
                for user in ADMINS:
                    await bot.send_message(user, msg)
            except:
                pass
        except asyncpg.exceptions.UniqueViolationError:
            await message.answer(f"Hurmatli Foydalanuvchi siz Bot ga a'zo bo'lgansiz bemalol foydalanishingiz mumkin.")
    else:
        btn = await show_channels()
        context = f"Assalomu alaykum, xurmatli <b>{message.from_user.full_name}</b>\nUniversal tarjimon botga xush kelibsiz.\nBotni ishlatishdan oldin quyidagi kanallarga obuna bo'ling 👇\n\n" \
                  f"A'zo bo'lganingizdan so'ng \"✅ A'zo Bo'ldim\" tugmasini bosing."
        await message.answer(text=context, reply_markup=btn)

@dp.callback_query_handler(text='sub_channel_done')
async def check_sub(call: CallbackQuery):

    async def is_subs(message):
        for channel in CHANNELS:
            check = await bot.get_chat_member(chat_id='-100' + str(channel[1]), user_id=message.id)
            if check.status == 'left':
                return False

        return True

    che_subs = await is_subs(call["from"])
    if che_subs:
        await call.message.delete()
        try:
            await db.add_user(
                telegram_id=call.from_user.id,
                full_name=call.from_user.full_name,
                username=call.from_user.username
            )
            await call.message.answer(f"Assalomu alaykum, {call.from_user.full_name}!\n<b>Universal Tarjimon Botiga</b> xush kelibsiz!")
            await call.message.answer("Xabaringizni yuboring: ")
            count = await db.select_all_user()
            msg = f"{call.from_user.full_name} bazaga qo'shildi.\nBazada {len(count)} ta foydalanuvchi bor."
            try:
                for user in ADMINS:
                    await bot.send_message(user, msg)
            except:
                pass
        except asyncpg.exceptions.UniqueViolationError:
            await call.message.answer(f"Hurmatli Foydalanuvchi siz Bot ga a'zo bo'lgansiz bemalol foydalanishingiz mumkin.")
    else:
        await call.answer(text="Berilgan kanallarga obuna bo'ling !",show_alert=True)
