import aiogram
import requests
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

btnHello = KeyboardButton("Готово")
greet_kb =  ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(btnHello)

inline_btn_1 = InlineKeyboardButton('Первая кнопка!', callback_data='button1')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)




button1 = KeyboardButton('/photo')
button2 = KeyboardButton('/note')
button3 = KeyboardButton('/info')
button4 = KeyboardButton('/create')
button5 = KeyboardButton('/history')

clean_kb = ReplyKeyboardMarkup(resize_keyboard=True).row(
    button1, button2, button3
).row(
    button4, button5
)


da = KeyboardButton('Да')
net = KeyboardButton('Нет')

buttons = ReplyKeyboardMarkup(resize_keyboard=True).row(da, net).add(
  KeyboardButton('Отменить'))


hide_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(net)



# Спор, между роботом и человеком
#@dp.message_handler()
#async def discuss(msg: types.Message):
#  if msg.text == 'Шлюхи аргумент':
#	await bot.send_message('аргумент не нужен, пидор обнаружен', reply_markup=kb.discuss_main)
#  elif msg.text == 'Пидор засекречен, твой анал не вечен':
#	await bot.send_message('анал мой вечен, твой анал помечен', reply_markup=kb.discuss_main)
#  elif msg.text == 'Мой замаскирован, твой уже разорван':
#	await bot.send_message('мой анал воссоздан, твой уже был продан!', reply_markup=kb.discuss_main)
#  elif msg.text == 'Пидрила...':
#	await bot.send_message('Хахахах, я переиграл тебя!', reply_markup=kb.discuss_main)
#  else:
#	await msg.reply('Сюда смотри!!!', reply_markup=kb.discuss_test)

discuss = KeyboardButton('Шлюхи аргумент')
discuss1 = KeyboardButton('Пидор засекречен, твой анал не вечен')
discuss2 = KeyboardButton('Мой замаскирован, твой уже разорван')
discuss3 = KeyboardButton('Пидрила...')
discuss_main = ReplyKeyboardMarkup(resize_keyboard=True).row(discuss, discuss1, discuss2).add(discuss3)
