from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command


from utils.misc.extra import WordFilter

from loader import dp, db



@dp.message_handler(commands="words")
async def select_word(message: types.Message):
    count = message.get_args()
    words = db.get_words(limit=int(count))
    text = ""
    for word in words:
        text+= f"{word[0]} - {word[1]}\n"
    await message.answer(text)


@dp.message_handler(Command("clear"))
async def clear_db(message: types.Message):
    db.clear_word()
    await message.answer("Baza tozalandi")
    
@dp.message_handler(Command("add"))
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("So'zlarni yuboring...")
    await state.set_state("add_word")


@dp.message_handler(state="add_word", commands="stop")
async def stop_handler(message: types.Message, state: FSMContext):
    await message.answer("So'z qo'shish yakunlandi")
    await state.finish()


@dp.message_handler(state="add_word")
async def enter_email(message: types.Message, state: FSMContext):
    text = message.text
    test = WordFilter(text)
    w = test.list_uz_en()
    print(w)
    for i in w:
        print(i[0], i[1])
        db.add_word(eng=i[0], uzb=i[1])
    await message.answer("Lug'atlar qo'shildi")

