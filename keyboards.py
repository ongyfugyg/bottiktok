from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

def menu_kb():
	button1 = KeyboardButton('Загрузить файл')
	button2 = KeyboardButton('Мои файлы')
	menu_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	menu_kb.add(button1)
	menu_kb.add(button2)
	return menu_kb
def back_kb():
	button1 = KeyboardButton('Отмена')
	back_kb1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	back_kb1.add(button1)
	return back_kb1
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def admin_menu():
	button2 = KeyboardButton('Рассылка')
	button3 = KeyboardButton('Назад')
	admin1_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	admin1_kb.add(button2)
	admin1_kb.add(button3)
	return admin1_kb
def back_2():
	back_kb1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	button = KeyboardButton('Отмена')
	back_kb1.add(button)
	return back_kb1
