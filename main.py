import os, re, configparser, requests
import urllib
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from aiogram.utils.helper import Helper, HelperMode, ListItem
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import urllib.request
from tiktok_downloader import snaptik

config = configparser.ConfigParser()
config.read("settings.ini")
TOKEN = config["tgbot"]["token"]

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

def download_video(video_url, name):
	r = requests.get(video_url, allow_redirects=True)
	content_type = r.headers.get('content-type')
	if content_type == 'video/mp4':
		open(f'./videos/video{name}.mp4', 'wb').write(r.content)
		open(f'./videos/audio{name}.mp3', 'wb').write(r.content)
	else:
		pass

if not os.path.exists('videos'):
	os.makedirs('videos')
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
	await bot.send_message(chat_id=message.chat.id, text='📼 Привет, я помогу тебе скачать видео с TikTok. \n/help - инструкция как скачать видео', reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
	await bot.send_message(chat_id=message.chat.id, text='Скопируй ссылку на видео TikTok и отправь её мне:')

@dp.message_handler(content_types=['text'])
async def text(message: types.Message):
	if message.text.startswith('https://www.tiktok.com'):
		await bot.send_message(chat_id=message.chat.id, text='Ожидайте...')
		video_url = message.text
		try:
			await bot.send_message(chat_id=message.chat.id, text='Скачиваю видео...')
			snaptik(video_url).get_media()[0].download(f"./videos/result_{message.from_user.id}.mp4")
			snaptik(video_url).get_media()[1].download(f"./videos/result_{message.from_user.id}.mp3")
			path = f'./videos/result_{message.from_user.id}.mp4'
			path_music = f'./videos/result_{message.from_user.id}.mp3'
			with open(f'./videos/result_{message.from_user.id}.mp4', 'rb') as file:
				await bot.send_video(
					chat_id=message.chat.id,
					video=file,
					caption='Вот твое видео:'
					)
			os.remove(path)
			with open(f'./videos/result_{message.from_user.id}.mp3', 'rb') as file:
				await bot.send_audio(
					chat_id=message.chat.id,
					audio=file,
					caption='Вот музыка видео:'
					)
			os.remove(path_music)
		except:
			await bot.send_message(chat_id=message.chat.id, text='Ошибка при скачивании, неверная ссылка, видео было удалено или я его не нашел.')
	elif message.text.startswith('https://vm.tiktok.com') or message.text.startswith('http://vm.tiktok.com'):
		await bot.send_message(chat_id=message.chat.id, text='Ожидайте...')
		video_url = message.text
		try:
			await bot.send_message(chat_id=message.chat.id, text='Скачиваю видео...')
			snaptik(video_url).get_media()[0].download(f"./videos/result_{message.from_user.id}.mp4")
			snaptik(video_url).get_media()[1].download(f"./videos/result_{message.from_user.id}.mp3")
			path = f'./videos/result_{message.from_user.id}.mp4'
			path_music = f'./videos/result_{message.from_user.id}.mp3'
			with open(f'./videos/result_{message.from_user.id}.mp4', 'rb') as file:
				await bot.send_video(
					chat_id=message.chat.id,
					video=file,
					caption='Вот твое видео:'
					)
			os.remove(path)
			with open(f'./videos/result_{message.from_user.id}.mp3', 'rb') as file:
				await bot.send_audio(
					chat_id=message.chat.id,
					audio=file,
					caption='Вот музыка видео:'
					)
			os.remove(path_music)
		except:
			await bot.send_message(chat_id=message.chat.id, text='Ошибка при скачивании, неверная ссылка, видео было удалено или я его не нашел.')
	else:
		await bot.send_message(chat_id=message.chat.id, text='Я тебя не понял, отправь мне ссылку на видео TikTok.')
if __name__ == "__main__":
	# Запускаем бота
	executor.start_polling(dp, skip_updates=True)