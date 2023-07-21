import logging
from aiogram import Bot, Dispatcher, executor
from aiogram.types import *

logging.basicConfig(level=logging.INFO)
TOKEN = "5990277666:AAENsS9RNpOBeohJb-SKqXecpAj_Hb3oQUE"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

songs = [
    '',
    'CQACAgIAAxkBAAPNZI2BorDs5GLCYK0MRJ7xVyLxLDwAAossAAICGRlIN7dWpsJmKC8vBA', 
    'CQACAgIAAxkBAAPOZI2BolVNdSeGF5JXuhDufrlOSygAAlsnAAIvpHBKBEBkQMtz1RYvBA', 
    'CQACAgIAAxkBAAPPZI2BolhwPj_WSCKL4y9BIQOWSrQAAlYsAALOWllIzAunCl1yVjMvBA', 
    'CQACAgIAAxkBAAPQZI2BogeAHD4v2gvXzESIkLDVZoMAAnwwAAI-s6lL90fPaQEr4AovBA', 
    'CQACAgIAAxkBAAPRZI2BooVhXo-llXoDdQgAAVPRYPRqAAK6LAAChClISv0LPNftVbQSLwQ', 
    'CQACAgIAAxkBAAPSZI2BokFl1rIccyD44k2pTLkI3cAAAqwzAALxfJhLm_UZUrHwy1cvBA', 
    'CQACAgIAAxkBAAPTZI2BohEx7KMwkbL2tAQWOJXIf8cAAlEpAAKfzMhLkN31FKv0jCkvBA', 
    'CQACAgIAAxkBAAPUZI2BosZjhcwBfF-0PK0i9xB2DX8AAkcyAAIv8-FLungBOOK6fYwvBA', 
    'CQACAgIAAxkBAAPVZI2Bot3ecJc8_pliv1GY0nj1awYAAr4oAAJIq6FJ1OJzxSqsuV0vBA', 
    'CQACAgIAAxkBAAPWZI2BohOLy7__KIUhsKdfmZXc_iQAAhAnAAL1c-hINqzGzWaCfzIvBA'
]

btn = InlineKeyboardMarkup(row_width=5)
btn.add(
    InlineKeyboardButton("1", callback_data="song:1"),
    InlineKeyboardButton("2", callback_data="song:2"),
    InlineKeyboardButton("3", callback_data="song:3"),
    InlineKeyboardButton("4", callback_data="song:4"),
    InlineKeyboardButton("5", callback_data="song:5"),
    InlineKeyboardButton("6", callback_data="song:6"),
    InlineKeyboardButton("7", callback_data="song:7"),
    InlineKeyboardButton("8", callback_data="song:8"),
    InlineKeyboardButton("9", callback_data="song:9"),
    InlineKeyboardButton("10", callback_data="song:10"),
)


@dp.message_handler(commands=['start'])
async def start_bot(message: Message):
    await message.answer("Musiqa botga xush kelibsiz. /list")

@dp.message_handler(commands=['list'])
async def music_list_bot(message: Message):
    context = """Musiqalar:\n
1. Jaloliddin ahmadaliyev
2. Ozoda Nursaidova - Alamlar (Remix)
3. Shoxruxbek Ergashev – Jonimni Kuydirgan ozorlaringdan
4. Jahongir Otajonov – Bom Bom
5. Muhammadziyo - Tabibim
6. Jaloliddin Ahmadaliyev – Sen qorqma u daydi
7. Xojiakbar Ruzmetov – Men telbami yo majnun kuyarman yor ishqida
8. Shoxruxbek Ergashev - Sevgimni olardim bozorlaringdan
9. Ozoda Nursaidova – Jichcha Yomonman
10. Jaloliddin Ahmadaliyev - Ketavering yalinmayman"""
    await message.answer(context, reply_markup=btn)


@dp.callback_query_handler(text_contains='song:')
async def get_song(call: CallbackQuery):
    # "song:8" ==> ["song", "8"]
    song_id = call.data.split(":")[-1]
    await call.message.answer_audio(audio=songs[int(song_id)])


# @dp.message_handler(content_types=['audio'])
# async def ttt(message: Message):
#     global songs
#     songs.append(
#         message.audio.file_id
#     )

if __name__ == "__main__":
    executor.start_polling(dp)