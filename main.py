
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
import asyncio
import random

players = {
    "first_id": "",
    "second_id": "",
    "first_username": "",
    "second_username" : ""
}
bot = Bot(token="5515760551:AAGIAaCgzKKj81eT0djsI3rH8k-pV7wJqgg")
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def run(message: Message):
    user_id = message.from_user.id
    kb = InlineKeyboardMarkup().add(InlineKeyboardButton(text="Принять игру", callback_data=f"{user_id}~accept"))
    global players
    players["first_id"] = user_id
    players["first_username"] = message.from_user.username
    await message.answer(f"Игрок @{message.from_user.username} предложил вам игру", reply_markup=kb)
@dp.callback_query_handler()
async def call_handler(call: CallbackQuery):
    if call.data.split("~")[1] == "accept":
        global players
        players["second_id"] = call.from_user.id
        players["second_username"] = call.from_user.username
        if call.from_user.id != players["second_username"]:
            choices = ["Орёл", "Решка"]
            await call.message.edit_text(f"@{players['second_username']} - Орёл\n@{players['first_username']} - Решка\nМонетка подброшена - ")
            await asyncio.sleep(0.5)
            await call.message.edit_text(f"@{players['second_username']} - Орёл\n@{players['first_username']} - Решка\nМонетка подброшена - 🌕")
            await asyncio.sleep(0.5)
            await call.message.edit_text(f"@{players['second_username']} - Орёл\n@{players['first_username']} - Решка\nМонетка подброшена - 🌑")
            await asyncio.sleep(0.5)
            await call.message.edit_text(f"@{players['second_username']} - Орёл\n@{players['first_username']} - Решка\nМонетка подброшена - 🌕")
            await asyncio.sleep(0.5)
            await call.message.edit_text(f"@{players['second_username']} - Орёл\n@{players['first_username']} - Решка\nМонетка подброшена - 🌑")
            ch = choices[random.randint(0, 1)]
            await asyncio.sleep(0.5)
            await call.message.edit_text(f"@{call.from_user.username} - Орёл\n@{players['first_username']} - Решка\nМонетка подброшена - {ch}")
            await asyncio.sleep(0.2)
            await call.message.edit_text(f"@{call.from_user.username} - Орёл\n@{players['first_username']} - Решка\nМонетка подброшена - {ch}, поздравляем с победой @{players['first_username'] if ch == 'Решка' else players['second_username']}!")

    # await call.message.answer(call.data)
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
