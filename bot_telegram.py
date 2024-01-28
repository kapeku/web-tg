
import aiogram
from aiogram import Bot, Dispatcher, executor, types

import json, string

bot = Bot(token='6385074249:AAHni1t45SL6uiaz5ceUl73lr9gJXGKq6lw')
dp = Dispatcher(bot)

async def on_startup(_):
	print('Бот вышел в онлайн')

'''******************************КЛИЕНТСКАЯ ЧАСТЬ*******************************************'''
@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, 'Приятного аппетита')
		await message.delete()
	except:
		await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/Pizza_SheefBot')

@dp.message_handler(commands=['Режим_работы'])
async def pizza_open_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'Вс-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00')

@dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'ул. Колбасная 15')


# @dp.message_handler(commands=['Меню'])
# async def pizza_menu_command(message : types.Message):
# 	for ret in cur.execute('SELECT * FROM menu').fetchall():
# 	   await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')
'''*******************************АДМИНСКАЯ ЧАСТЬ*******************************************'''

'''*********************************ОБЩАЯ ЧАСТЬ*********************************************'''

@dp.message_handler()
async def echo_send(message : types.Message):
	if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
		.intersection(set(json.load(open('мат.json')))) != set():
		await message.reply('Маты запрещены')
		await message.delete()

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
