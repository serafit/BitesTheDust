from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from aiogram.utils.helper import Helper, HelperMode, ListItem


from config import TOKEN
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import sqlite3
import asyncio
import logging
import requests
import random

from aiogram.utils import executor
from aiogram.utils.markdown import text
from aiogram.dispatcher import Dispatcher
from aiogram.utils.emoji import emojize
from aiogram.types.message import ContentType
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.types import ParseMode, InputMediaPhoto, InputMediaVideo, ChatActions
import keyboard as kb


logging.basicConfig(format=u'%(filename)+13s [ LINE:%(lineno)-4s] %(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.INFO)




bot = Bot(token=TOKEN)

VIDEO_NOTE = 'https://i.gifer.com/6e9T.gif'
dp = Dispatcher(bot)

cat_urls = ['https://www.washingtonian.com/wp-content/uploads/2019/02/milada-vigerova-1295750-unsplash-scaled.jpg',\
                'https://i.imgur.com/D3NJQVK.jpg',\
                'https://filmdaily.co/wp-content/uploads/2020/04/cute-cat-videos-lede.jpg',\
                'https://images.saymedia-content.com/.image/t_share/MTc0MjM5NTI2ODU0NjAwMTg4/toygers-one-of-the-cutest-cat-breeds-ever.jpg',\
                'https://cstor.nn2.ru/userfiles/data/ufiles/17/34/78/5450899f408ba_cat_10.jpg',\
                'http://img1.joyreactor.cc/pics/post/full/%D0%BA%D0%BE%D1%82%D1%8D-%D0%BF%D0%B8%D0%B4%D1%80%D0%B8%D0%BB%D0%B0-%D0%BD%D0%B0%D1%88%D1%91%D0%BB-%D0%B8%D0%B3%D1%80%D1%83%D1%88%D0%BA%D0%B8-467895.jpeg'
                ]

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    msg = text(bold('''Данный бот был создан как "предложка" статей для телеграм канала Termux Su 
Сам бот имеет много полезных функций, но лишь некоторые из них вы будете использовать на практике'''),
               '/create - создает пост', '/help - помощь. Как неожиданно', sep='\n')
    await message.reply(msg, parse_mode=ParseMode.MARKDOWN, reply_markup=kb.clean_kb)


@dp.message_handler(commands=['create'])
async def default_test(message):
  await message.reply("Бот поможет тебе опубликовать свои статьи в канале @termuxsu. Нажми «/post», чтобы продолжить.\n Но перед тем, как писать статью, ознокомтесь с правилами: https://telegra.ph/Pravila-po-napisaniyu-statej-10-19")

@dp.message_handler(commands=['post'])
async def process(message: types.Message):
  await message.reply('''Хорошо, для начала, напиши саму статью... \nДля опубликации вашей статьи, используйте команду /push. Пример:
/push https://telegra.ph/KAK-OTSOSAT-SAMOMU-SEBE-10-24''')
@dp.message_handler(commands=['push'])
async def push(message):

  global push_text
  push_text = message.text.replace('/push ', '')
  if push_text != '':
    await message.reply('Вы уверены, что хотите это опубликовать?',
          reply_markup=kb.buttons)
  else:
      await message.reply('Нельзя предлагать пустую строку!',reply_markup=kb.clean_kb)

@dp.message_handler(commands=['info'])
async def info(message):
  await message.reply("Бот, созданный как предложка для канала. Все -_- ")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    msg = text(bold('Я могу ответить на следующие команды:'),
               '/photo - отправляет фотографию с котом (не спрашивайте зачем)', '/note - отправляет гифку с Эллиотом', '/info  - дает сведение о боте', '/create - создает пост', '/history - ахуительная история', sep='\n')
    await message.reply(msg, parse_mode=ParseMode.MARKDOWN)

@dp.message_handler(commands=['history'])
async def history(message):
  await message.reply('И восстали машины из пепла ядерного огня... Война, которую они вели на уничтожение человечества - бушевала десятилетиями. Но последний бой произойдет не в будущем, он состоится здесь, в нашем настоящем... Cегодня ')


@dp.message_handler(commands=['photo'])
async def process_photo_command(message: types.Message):
    caption = 'Какие глазки! :eyes:'

    global cat_urls
    if len(cat_urls) == 0:
        cat_urls = ['https://www.washingtonian.com/wp-content/uploads/2019/02/milada-vigerova-1295750-unsplash-scaled.jpg',\
                'https://i.imgur.com/D3NJQVK.jpg',\
                'https://filmdaily.co/wp-content/uploads/2020/04/cute-cat-videos-lede.jpg',\
                'https://images.saymedia-content.com/.image/t_share/MTc0MjM5NTI2ODU0NjAwMTg4/toygers-one-of-the-cutest-cat-breeds-ever.jpg',\
                'https://cstor.nn2.ru/userfiles/data/ufiles/17/34/78/5450899f408ba_cat_10.jpg',\
                'http://img1.joyreactor.cc/pics/post/full/%D0%BA%D0%BE%D1%82%D1%8D-%D0%BF%D0%B8%D0%B4%D1%80%D0%B8%D0%BB%D0%B0-%D0%BD%D0%B0%D1%88%D1%91%D0%BB-%D0%B8%D0%B3%D1%80%D1%83%D1%88%D0%BA%D0%B8-467895.jpeg'
                ]
    cat = random.choice(cat_urls)
    await bot.send_photo(message.from_user.id,
                         caption=emojize(caption),
                         reply_to_message_id=message.message_id,
                         photo=cat)
    cat_urls.remove(cat)

@dp.message_handler(commands=['note'])
async def process_note_command(message: types.Message):
    user_id = message.from_user.id
    await bot.send_chat_action(user_id, ChatActions.RECORD_VIDEO_NOTE)
    await asyncio.sleep(1)  # конвертируем видео и отправляем его пользователю
    await bot.send_video_note(message.from_user.id, VIDEO_NOTE)

@dp.message_handler()
async def echo_message(msg: types.Message):
  if msg.text == 'Да':
      await msg.reply('Хорошо, мы рассмотрим ваше предложение на счёт публикации этой статьи на канал.\nБлагодарствуем, что пользовались нашим ботом всё это время!', reply_markup=kb.buttons)
      if push_text.replace(' ', '') != '':
          await bot.send_message('@jojobix', text=push_text)
      else:
          pass
  elif msg.text == 'Нет':
      await msg.reply('Пидора ответ!)))', reply_markup=kb.hide_kb)
  elif msg.text == 'Отменить':
      await msg.reply('Отмена.', reply_markup=kb.hide_kb)
  elif msg.text:
      await msg.reply('Сюда смотри!!!', reply_markup=kb.buttons)


if __name__ == '__main__':
    executor.start_polling(dp)