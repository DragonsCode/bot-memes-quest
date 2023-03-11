#By @Dragons_play
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.utils import executor
import aiogram
import asyncio
import config
import logging

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class Form(StatesGroup):
    test1 = State() 
    test2 = State() 
    test3 = State()
    test4 = State()
    test5 = State()
    test6 = State()
    test7 = State()
    test8 = State()
    test9 = State()
    test10 = State()
    test11 = State()
    test12 = State()
    name = State()

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.reply("Привет, напиши /help чтобы ознакомиться с инструкциями бота \nНапиши /tests чтобы начать прохождение тестов!")
@dp.message_handler(commands=['help'])
async def cmd_help(message: types.Message):
    await message.reply("Это бот-опросник по мемам, пройдите тест полностью, чтобы получить вашу анкету с вашими ответами, а потом можете пригласить друзей и свериться ответами и схожестью ваших вкусов в мемах! Напишите команду /tests чтобы начать прохождение тестов. При тестировании отвечайте `Да` или `Нет`, чтобы перейти к следующему вопросу с мемом. Мемов всего 12")
@dp.message_handler(commands=['tests'])
async def tests(message: types.Message):
    await Form.test1.set()
    await message.reply("Хорошо, тогда погнали!")
    await bot.send_photo(chat_id=message.chat.id, photo='https://yadi.sk/i/f9_8l58-3EwYqw')
    await message.answer("Вам нравится этот мем?")
    await message.answer("Отвечайте `Да` или `Нет`")
    await message.answer("Чтобы отменить тестирование напишите команду /cancel")


@dp.message_handler(state='*', commands='cancel')
@dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.finish()
    await message.reply('Тестирование отменено!')

@dp.message_handler(lambda message: message.text not in ["Да", "Нет"], state=Form.test1)
async def test1_invalid(message: types.Message):
    return await message.reply("Вы ответили не правильно. Напишите `Да` или `Нет` или же можете отменить тестирование командой /cancel")



@dp.message_handler(state=Form.test1)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test1'] = message.text

    await Form.next()
    await message.reply("Следующий второй мем")
    await bot.send_photo(chat_id=message.chat.id, photo='https://yadi.sk/i/iDVzdUrYCqVL9g')
    await message.answer("Вам нравится этот мем?")
    await message.answer("Отвечайте `Да` или `Нет`")
    await message.answer("Чтобы отменить тестирование напишите команду /cancel")


@dp.message_handler(lambda message: message.text not in ["Да", "Нет"], state=Form.test2)
async def test2_invalid(message: types.Message):
    return await message.reply("Вы ответили не правильно. Напишите `Да` или `Нет` или же можете отменить тестирование командой /cancel")

@dp.message_handler(state=Form.test2)
async def process_test2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test2'] = message.text

    await Form.next()
    await message.reply("Следующий третий мем")
    await bot.send_photo(chat_id=message.chat.id, photo='https://yadi.sk/i/ej273Jv0KKwtLg')
    await message.answer("Вам нравится этот мем?")
    await message.answer("Отвечайте `Да` или `Нет`")
    await message.answer("Чтобы отменить тестирование напишите команду /cancel")

@dp.message_handler(lambda message: message.text not in ["Да", "Нет"], state=Form.test3)
async def test3_invalid(message: types.Message):
    return await message.reply("Вы ответили не правильно. Напишите `Да` или `Нет` или же можете отменить тестирование командой /cancel")

@dp.message_handler(state=Form.test3)
async def process_test3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test3'] = message.text

    await Form.next()
    await message.reply("Следующий четвертый мем")
    await bot.send_photo(chat_id=message.chat.id, photo='https://yadi.sk/i/gmqWw0znN-qRLg')
    await message.answer("Вам нравится этот мем?")
    await message.answer("Отвечайте `Да` или `Нет`")
    await message.answer("Чтобы отменить тестирование напишите команду /cancel")


@dp.message_handler(lambda message: message.text not in ["Да", "Нет"], state=Form.test4)
async def test4_invalid(message: types.Message):
    return await message.reply("Вы ответили не правильно. Напишите `Да` или `Нет` или же можете отменить тестирование командой /cancel")

@dp.message_handler(state=Form.test4)
async def process_test4(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test4'] = message.text

    await Form.next()
    await message.reply("Следующий пятый мем")
    await bot.send_photo(chat_id=message.chat.id, photo='https://yadi.sk/i/OVDiQpjgKnYbfQ')
    await message.answer("Вам нравится этот мем?")
    await message.answer("Отвечайте `Да` или `Нет`")
    await message.answer("Чтобы отменить тестирование напишите команду /cancel")


@dp.message_handler(lambda message: message.text not in ["Да", "Нет"], state=Form.test5)
async def test5_invalid(message: types.Message):
    return await message.reply("Вы ответили не правильно. Напишите `Да` или `Нет` или же можете отменить тестирование командой /cancel")

@dp.message_handler(state=Form.test5)
async def process_test5(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test5'] = message.text

    await Form.next()
    await message.reply("Следующий шестой мем")
    await message.answer("Ого, вы уже на половине пути!")
    await bot.send_photo(chat_id=message.chat.id, photo='https://yadi.sk/i/ukOGO8MCzFhhWw')
    await message.answer("Вам нравится этот мем?")
    await message.answer("Отвечайте `Да` или `Нет`")
    await message.answer("Чтобы отменить тестирование напишите команду /cancel")


@dp.message_handler(lambda message: message.text not in ["Да", "Нет"], state=Form.test6)
async def test6_invalid(message: types.Message):
    return await message.reply("Вы ответили не правильно. Напишите `Да` или `Нет` или же можете отменить тестирование командой /cancel")

@dp.message_handler(state=Form.test6)
async def process_test6(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test6'] = message.text

    await Form.next()
    await message.reply("Следующий седьмой мем")
    await bot.send_photo(chat_id=message.chat.id, photo='https://yadi.sk/i/8B8GmcN1X2oGKA')
    await message.answer("Вам нравится этот мем?")
    await message.answer("Отвечайте `Да` или `Нет`")
    await message.answer("Чтобы отменить тестирование напишите команду /cancel")


@dp.message_handler(lambda message: message.text not in ["Да", "Нет"], state=Form.test7)
async def test7_invalid(message: types.Message):
    return await message.reply("Вы ответили не правильно. Напишите `Да` или `Нет` или же можете отменить тестирование командой /cancel")

@dp.message_handler(state=Form.test7)
async def process_test7(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test7'] = message.text

    await Form.next()
    await message.reply("Следующий восьмой мем")
    await bot.send_photo(chat_id=message.chat.id, photo='https://yadi.sk/i/CP1frNnPCobm3g')
    await message.answer("Вам нравится этот мем?")
    await message.answer("Отвечайте `Да` или `Нет`")
    await message.answer("Чтобы отменить тестирование напишите команду /cancel")


@dp.message_handler(lambda message: message.text not in ["Да", "Нет"], state=Form.test8)
async def test8_invalid(message: types.Message):
    return await message.reply("Вы ответили не правильно. Напишите `Да` или `Нет` или же можете отменить тестирование командой /cancel")

@dp.message_handler(state=Form.test8)
async def process_test8(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test8'] = message.text

    await Form.next()
    await message.reply("Следующий девятый мем, ещё немного и будет чудо")
    await bot.send_photo(chat_id=message.chat.id, photo='https://yadi.sk/i/Orqf7uUlS0Vtbw')
    await message.answer("Вам нравится этот мем?")
    await message.answer("Отвечайте `Да` или `Нет`")
    await message.answer("Чтобы отменить тестирование напишите команду /cancel")


@dp.message_handler(lambda message: message.text not in ["Да", "Нет"], state=Form.test9)
async def test9_invalid(message: types.Message):
    return await message.reply("Вы ответили не правильно. Напишите `Да` или `Нет` или же можете отменить тестирование командой /cancel")

@dp.message_handler(state=Form.test9)
async def process_test9(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test9'] = message.text

    await Form.next()
    await message.reply("Следующий десятый мем")
    await bot.send_photo(chat_id=message.chat.id, photo='https://yadi.sk/i/1Itjg06cHjGrIg')
    await message.answer("Вам нравится этот мем?")
    await message.answer("Отвечайте `Да` или `Нет`")
    await message.answer("Чтобы отменить тестирование напишите команду /cancel")


@dp.message_handler(lambda message: message.text not in ["Да", "Нет"], state=Form.test10)
async def test10_invalid(message: types.Message):
    return await message.reply("Вы ответили не правильно. Напишите `Да` или `Нет` или же можете отменить тестирование командой /cancel")

@dp.message_handler(state=Form.test10)
async def process_test10(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test10'] = message.text

    await Form.next()
    await message.reply("Следующий предпоследний одиннадцатый мем")
    await bot.send_photo(chat_id=message.chat.id, photo='https://yadi.sk/i/XXGvb69nMnx1HQ')
    await message.answer("Вам нравится этот мем?")
    await message.answer("Отвечайте `Да` или `Нет`")
    await message.answer("Чтобы отменить тестирование напишите команду /cancel")


@dp.message_handler(lambda message: message.text not in ["Да", "Нет"], state=Form.test11)
async def test11_invalid(message: types.Message):
    return await message.reply("Вы ответили не правильно. Напишите `Да` или `Нет` или же можете отменить тестирование командой /cancel")

@dp.message_handler(state=Form.test11)
async def process_test11(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test11'] = message.text

    await Form.next()
    await message.reply("И последний двенадцатый мем")
    await bot.send_photo(chat_id=message.chat.id, photo='https://yadi.sk/i/zcPCsmgzRsKDuw')
    await message.answer("Вам нравится этот мем?")
    await message.answer("Отвечайте `Да` или `Нет`")
    await message.answer("Чтобы отменить тестирование напишите команду /cancel")


@dp.message_handler(lambda message: message.text not in ["Да", "Нет"], state=Form.test12)
async def test12_invalid(message: types.Message):
    return await message.reply("Вы ответили не правильно. Напишите `Да` или `Нет` или же можете отменить тестирование командой /cancel")

@dp.message_handler(state=Form.test12)
async def process_test12(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test12'] = message.text

    await Form.next()
    await message.reply("А теперь скажите как вас зовут:")

@dp.message_handler(state=Form.name)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
#        username = "ID пользователя в телеграме: "
        usernick = "Имя пользователя: " + data['name']
        
        test1 = "Ваш ответ на первый мем: " + data['test1'] + "\n"
        test2 = "Ваш ответ на второй мем: " + data['test2'] + "\n"
        test3 = "Ваш ответ на третий мем: " + data['test3'] + "\n"
        test4 = "Ваш ответ на четвертый мем: " + data['test4'] + "\n"
        test5 = "Ваш ответ на пятый мем: " + data['test5'] + "\n"
        test6 = "Ваш ответ на шестой мем: " + data['test6'] + "\n"
        test7 = "Ваш ответ на седьмой мем: " + data['test7'] + "\n"
        test8 = "Ваш ответ на восьмой мем: " + data['test8'] +"\n"
        test9 = "Ваш ответ на девятый мем: " + data['test9'] + "\n"
        test10 = "Ваш ответ на десятый мем: " + data['test10'] + "\n"
        test11 = "Ваш ответ на одиннадцатый мем: " + data['test11'] + "\n"
        test12 = "Ваш ответ на двенадцатый мем: " + data['test12'] + "\n"
        
        test1t6 = test1 + test2 + test3 + test4 + test5 + test6
        test7t12 = test7 + test8 + test9 + test10 + test11 + test12
        testall = test1t6 + test7t12 + "\n \n"
        
        percent = 0
        if data['test1'] == "Да":
            percent += 8.333
        if data['test2'] == "Да":
            percent += 8.333
        if data['test3'] == "Да":
            percent += 8.333
        if data['test4'] == "Да":
            percent += 8.333
        if data['test5'] == "Да":
            percent += 8.333
        if data['test6'] == "Да":
            percent += 8.333
        if data['test7'] == "Да":
            percent += 8.333
        if data['test8'] == "Да":
            percent += 8.333
        if data['test9'] == "Да":
            percent += 8.333
        if data['test10'] == "Да":
            percent += 8.333
        if data['test11'] == "Да":
            percent += 8.333
        if data['test12'] == "Да":
            percent += 8.333
        
        percent2 = 0
        if data['test1'] == "Нет":
            percent2 += 8.333
        if data['test2'] == "Нет":
            percent2 += 8.333
        if data['test3'] == "Нет":
            percent2 += 8.333
        if data['test4'] == "Нет":
            percent2 += 8.333
        if data['test5'] == "Нет":
            percent2 += 8.333
        if data['test6'] == "Нет":
            percent2 += 8.333
        if data['test7'] == "Нет":
            percent2 += 8.333
        if data['test8'] == "Нет":
            percent2 += 8.333
        if data['test9'] == "Нет":
            percent2 += 8.333
        if data['test10'] == "Нет":
            percent2 += 8.333
        if data['test11'] == "Нет":
            percent2 += 8.333
        if data['test12'] == "Нет":
            percent2 += 8.333
        
        ysum = 0
        if data['test1'] == "Да":
            ysum += 1
        if data['test2'] == "Да":
            ysum += 1
        if data['test3'] == "Да":
            ysum += 1
        if data['test4'] == "Да":
            ysum += 1
        if data['test5'] == "Да":
            ysum += 1
        if data['test6'] == "Да":
            ysum += 1
        if data['test7'] == "Да":
            ysum += 1
        if data['test8'] == "Да":
            ysum += 1
        if data['test9'] == "Да":
            ysum += 1
        if data['test10'] == "Да":
            ysum += 1
        if data['test11'] == "Да":
            ysum += 1
        if data['test12'] == "Да":
            ysum += 1
        
        nsum = 0
        if data['test1'] == "Нет":
            nsum += 1
        if data['test2'] == "Нет":
            nsum += 1
        if data['test3'] == "Нет":
            nsum += 1
        if data['test4'] == "Нет":
            nsum += 1
        if data['test5'] == "Нет":
            nsum += 1
        if data['test6'] == "Нет":
            nsum += 1
        if data['test7'] == "Нет":
            nsum += 1
        if data['test8'] == "Нет":
            nsum += 1
        if data['test9'] == "Нет":
            nsum += 1
        if data['test10'] == "Нет":
            nsum += 1
        if data['test11'] == "Нет":
            nsum += 1
        if data['test12'] == "Нет":
            nsum += 1
        
        mf12 = " мемов из 12, в процентах: "
        nlm1 = "\n Вам не понравилось "
        text2 = "Покажите свои ответы друзьям, приглашайте их сюда по этой ссылке: @Testoviy_oprosnik_bot и сверьтесь с ответами с ними, узнайте какой вкус на мемы у своих друзей!\n \n"
        text = text2 + usernick + "\n \n" + testall + "Вам понравилось "
        await bot.send_message(message.chat.id, text = f"{text} {ysum} {mf12} {percent} {nlm1} {nsum} {mf12} {percent2}")
#        await bot.send_message(message.chat.id, text, ysum, mf12, percent, nlm1, nsum, mf12, percent2)
    await state.finish()

async def on_startup(dp):
    await bot.set_my_commands([types.BotCommand('start',
                                                'Начать диалог с ботом'),
                               types.BotCommand('help',
                                                'Помощь и инструкции к боту'),
                                types.BotCommand('tests',
                                                'Начать тестирование на мемы')])



print("Made by @Dragons_play")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)






