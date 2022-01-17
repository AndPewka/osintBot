from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton(text="Справка№1")

		],
		[
			KeyboardButton(text="Номер"),
			KeyboardButton(text="Спам"),
			KeyboardButton(text="Логин")

		],
				[
			KeyboardButton(text="Авто"),

		],
	],
    resize_keyboard=True
)

PhoneInfo = ReplyKeyboardMarkup(
	keyboard = [
	[
		KeyboardButton(text="Справка№4"),
		KeyboardButton(text="Главная")
	],
	],
	resize_keyboard=True

	)

PhoneSpam = ReplyKeyboardMarkup(
	keyboard = [
		[
			KeyboardButton(text="Справка№2"),
			KeyboardButton(text="Главная")

		],
		[
			KeyboardButton(text="Начать")
		],
	],
	resize_keyboard=True
)

LoginSearch = ReplyKeyboardMarkup(
	keyboard = [
		[

			KeyboardButton(text ="Справка№3"),
			KeyboardButton(text ="Главная")
		],
		[
			KeyboardButton(text ="Начать поиск"),
			KeyboardButton(text ="Получить данные")
		],
	],
	resize_keyboard=True
)

registration = ReplyKeyboardMarkup(
	keyboard =[
		[
		KeyboardButton(text = "Вход",request_contact=True),
		KeyboardButton(text = "Пробная версия")
		],	
	],
	resize_keyboard=True




	)
