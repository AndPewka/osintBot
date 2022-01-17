#Variable

#library
import aiogram
from aiogram.types import Message
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram import types
import os
import datetime

#local files
from nameplate import *
from main import bot, dp
from config import admin_id
from keyboards import menu,PhoneSpam,registration,LoginSearch,PhoneInfo
from river import river_bomber,river_sherlock,getcontact
from help import *
#from base import create_target_Search,create_base_person,create_bomber_target
from base import (base_regisrt,check_registr,trial_to_reg,
	update_bomber_target,check_bomber_target,
	update_search_target,check_search_target,
	update_flag,check_flag,
	update_statistics,get_statistics,)

#выполняется команда при запуске
async def starter(*args):
	await bot.send_message(chat_id=admin_id, text="Бот запущен",reply_markup = menu)


##############################################################################################################################################################################
@dp.message_handler(commands=['start'])
async def start_message(message : Message):
	user_id = message.chat.id
	if check_registr(user_id) == "reg" or check_registr(user_id) == "trial":
		await message.answer(text="Главная.",reply_markup = menu)
	else:
		await message.answer(text="Зарегистрируйтесь !\nЛибо можете активировать пробный перид на 1 день.",reply_markup = registration)



#если пишут /menu выполняется
@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
	await message.answer("Выбери услугу из списка ниже:", reply_markup=menu)
##############################################################################################################################################################################
#обработка событий формы /menu
@dp.message_handler(Text(equals=["Номер", "Спам", "Логин","Справка№1","Авто"]))
async def malware(message: Message):
	text = message.text
	user_id = message.chat.id
	
	if check_registr(user_id) == "reg" or check_registr(user_id) == "trial":
		if text == "Справка№1":
			await message.answer(reference_1, reply_markup=menu)

		if text == "Номер":
			count = get_statistics(1)
			await message.answer("Вы выбрали сервис с поиском имени абонента.\nВсего поисков :" + str(count) +
	"\nВведите номер в любом формате" + "\nПримерное время ожидания - минута.", reply_markup=PhoneInfo)
			update_flag(message.chat.id,"1",1)

		if text == "Логин":
			count = get_statistics(4)
			await message.answer("Вы выбрали сервис поиска по имени пользователя\n" + "Всего поисков : " + str(count) +
	"""\nВведите логин.
	Дальше нажмите "Начать поиск",""", reply_markup=LoginSearch)
			update_flag(message.chat.id,"1",2)

		if text == "Баланс":
			await message.answer("Данный сервис пока-что бесплатен.", reply_markup=menu)


		if text == "Спам":
			count  = get_statistics(3)
			await message.answer("Вы выбрали услугу смс-спамма :\n" + "Всего отправлено спама : " + str(count) +
	"""\nВведите номер в виде 8**********.
	Введите колличество спама(200 Максимум).
	Введите,пожалуйста,номер и колличество в два сообщения.""", reply_markup=PhoneSpam)

			update_flag(message.chat.id,"1",3)
		if text == "Авто":
			await message.answer(text="""Данная функция находиться на этапе разбработки!""",reply_markup = menu)
			
	else:
		await message.answer(text="""Зарегистрируйтесь!""",reply_markup = registration)

##############################################################################################################################################################################
#интерфейс бомбера
@dp.message_handler(Text(equals=["Справка№2","Начать"]))
async def malware(message: Message):
	text = message.text
	user_id = message.chat.id
	if check_registr(user_id) == "reg" or check_registr(user_id) == "trial":
		if check_flag(message.chat.id,4) == "0":
			if text == "Начать":

				update_flag(message.chat.id,"1",4)
				massive = check_bomber_target(message.chat.id)
				number = massive[0][0]
				count = massive[0][1]
				update_statistics(3,count)
				if river_bomber(message.chat.id,number,count) == False:
					await message.answer("В данный момент эта услуга используется другим человеком.Вы встали в очередь. ".format(number,count), reply_markup=PhoneSpam)
				else:
					await message.answer("Атака на номер :" + str(number) +  " в колличестве " + count + " началась! ", reply_markup=PhoneSpam)
					await bot.send_message(chat_id=admin_id, text="пользователь : " + str(user_id) + " запросил атаку на " + str(number))
				del massive
		else:
			await message.answer("Прошлая атака еще не была закончена.", reply_markup=PhoneSpam)

		if text == "Справка№2":
			massive = check_bomber_target(message.chat.id)
			number = massive[0][0]
			count = massive[0][1]
			await message.answer(text="Выбран цель для атаки :\nНомер - " + str(number) + "\nКолличество смс - " + str(count) +
				"\nЭта функция отправляет смс-спам на любой номер РФ.Пожалуйста,пользуйтесь ей только в крайнем случае и имейте в виду,что эта функция незаконна. Статьи 272 УК РФ.",reply_markup = PhoneSpam)
	else:
		await message.answer(text="""Зарегистрируйтесь!""",reply_markup = registration)
##############################################################################################################################################################################
#ИНТТЕРФЕЙС GETCONTACT
@dp.message_handler(Text(equals=["Справка№4"]))
async def malware(message: Message):
	text = message.text
	if check_registr(user_id) == "reg" or check_registr(user_id) == "trial":

		if text == "Справка№4":
			await message.answer("""Введите номер в виде 8**********
	Данная функция не работает на зарубежные номера.""", reply_markup=PhoneInfo)
	else:
		await message.answer(text="""Зарегистрируйтесь !""",reply_markup = registration)


##############################################################################################################################################################################
#ПОИСК ЛОГИНА

@dp.message_handler(Text(equals=["Справка№3","Начать поиск","Получить данные"]))
async def malware(message: Message):

	text = message.text
	user_id = message.chat.id
	if check_registr(user_id) == "reg" or check_registr(user_id) == "trial":

		if text =="Справка№3":
			await message.answer(text="""Ищет сайты у которых в URL есть имя,которое вы введете.
	Пользователи зачастую регистрируются под одним логином,тем самым этой функцией вы можете посмотреть все сайты,где зарегистрирован этот пользователь,
	например при вводе Никнейма test_login вам выдаст ссылки соц.сетей, где у человека ток же самый никнейм,Например :
	https://vk.com/test_login
	https://www.instagram.com/test_login.""",reply_markup = LoginSearch)


	
		if text == "Начать поиск":
			if check_flag(message.chat.id,5) == "0":
				if river_sherlock:
					name = check_search_target(message.chat.id)
					await bot.send_message(chat_id=admin_id, text="пользователь : " + str(user_id) + " запросил поиск на " + str(name))
					river_sherlock(message.chat.id,name)
					update_flag(message.chat.id,"1",5)
					await message.answer(text="Поиск начался.Примерное время ожидания - 30 минут.",reply_markup = LoginSearch)
			else:
				await message.answer(text="Нажмите на ПОЛУЧИТЬ ДАННЫЕ,чтобы совершить следующий поиск.",reply_markup = LoginSearch)
				

		if text == "Получить данные":
			login_name=""
			count = 0
			name = check_search_target(message.chat.id)
			if os.path.exists(name+".txt"):
				with open(name+".txt","r") as file:
					data = file.read()
				if data == "":
					await message.answer(text="""Проверка еще идет.\n""" + data,reply_markup = LoginSearch)
				else:
					update_statistics(4)
					update_flag(message.chat.id,"0",5)
					for i in data:
						login_name = login_name + i
						if i == "\n":
							
							count += 1
						if count == 25:
							await message.answer(text="""Совпадение имени этого пользователя были найдены на следующих сайтах : \n""" + login_name,reply_markup = LoginSearch)
							login_name = ""
							count = 0
					await message.answer(text="""Совпадение имени этого пользователя были найдены на следующих сайтах : \n""" + login_name,reply_markup = LoginSearch)
					os.remove(name+".txt")
			else:
				await message.answer(text="""Чтобы получить данные начните поиск !\n""",reply_markup = LoginSearch)



	else:
		await message.answer(text="""Зарегистрируйтесь!""",reply_markup = registration)


##############################################################################################################################################################################
#РЕГИСТРАЦИЯ
@dp.message_handler(content_types=["contact"])
async def registr(message: Message):
	phone_number = message.contact.phone_number
	user_id = str(message.contact.user_id)
	name = str(message.contact.first_name)
	last_name = str(message.contact.last_name)
	with open("registration.txt","a") as file:
		file.write(str(message.contact) + "\n")

	trial_to_reg(user_id)
	base_regisrt(phone_number,user_id,name,last_name)
	await bot.send_message(chat_id=admin_id,text = "Пользователь : " + str(phone_number) + " был зарегистрирован !")
	await message.answer(text="Вы успешно зарегистрировались !",reply_markup = menu)

#Пробный перод
@dp.message_handler(Text(equals=["Пробная версия"]))
async def malware(message: Message):
	user_id = message.chat.id
	text = message.text

	if check_registr(user_id) == "trial_time":
		await message.answer(text="Ваш пробный пероид истек, перейдите к РЕГИСТРАЦИИ.",reply_markup = registration)

	else:
		now = datetime.datetime.now()
		now = str(now.date())
		base_regisrt("not registr",user_id,"trial",now)
		await message.answer(text="""Вы активировали пробный период !\nПродолжительность пробной версии - 1 день""",reply_markup = menu)
		await bot.send_message(chat_id=admin_id, text="Пользователь : " + str(user_id) + " активировал пробный период !",reply_markup = menu)


##############################################################################################################################################################################
#await message.answer(f"Вы выбрали {message.text}. Спасибо", reply_markup=ReplyKeyboardRemove()) # убирается клавиатура






@dp.message_handler()
async def echo(message: Message):
	text = message.text
	user_id = message.chat.id
	if check_registr(user_id) == "reg" or check_registr(user_id) == "trial":
		


		if text == "Главная":
			await message.answer(text="Главное меню",reply_markup = menu)
			update_flag(message.chat.id,"0",1)
			update_flag(message.chat.id,"0",2)
			update_flag(message.chat.id,"0",3)

		if check_flag(message.chat.id,1) == "1":
			if (text[0:1] == "8" or text[0:2] == "+7" or text[0:1] == "7") and len(text) > 10:
				text = trans_tele(text)
				await bot.send_message(chat_id=admin_id, text="пользователь : " + str(user_id) + " запросил поиск на " + str(text))
				result = []
				avitolist = ""
				dromlist = ""
				result = getcontact(text)

				update_statistics(1)
				name = result[0]
				if name == "" or name == "Not Found":
					name = "Данного номера нет в базах данных"

				region = result[1]
				operator = result[2]
				links_avito = result[3]
				links_drom = result[4]
				if links_avito == []:
					avitolist = "объявлений на сайте по этому номеру не найдены."
				else:
					for i in links_avito:
						avitolist = avitolist + i + "\n"
				if links_drom == []:
					dromlist = "объявлений на сайте по этому номеру не найдены."
				else:
					for i in links_drom:
						dromlist = dromlist + i + "\n"
				await message.answer(text="""Владелец телефона - {}\n
Регион проживания - {}
Оператор сотовой связи - {}
Ссылки с avito.ru - {}
Ссылки с drom.ru - {}
		""".format(name,region,operator,avitolist,dromlist),reply_markup = PhoneInfo)
			else:
				await message.answer(text="Неверный формат номера!",reply_markup = PhoneInfo)


		if check_flag(message.chat.id,3) =="1" and len(text) == 11 and text[0] == "8":
			update_bomber_target(message.chat.id,text,0)
			await message.answer(text="Вы ввели номер ---> " + text,reply_markup = PhoneSpam)


		if check_flag(message.chat.id,3) =="1" and int(text) <= 200:
			update_bomber_target(message.chat.id,text,1)
			await message.answer(text="Вы ввели колличество ---> " + text,reply_markup = PhoneSpam)

		if check_flag(message.chat.id,2) == "1":
			if check_flag(message.chat.id,5) == "0":
				name = check_search_target(message.chat.id)
				if os.path.exists(name+".txt"):
					await message.answer(text="""Проверка еще идет.Вы не можете вводить новый никнейм !\n""",reply_markup = LoginSearch)
				else:
					update_search_target(message.chat.id,text)
					await message.answer(text="Вы ввели имя пользователя ---> " + text,reply_markup = LoginSearch)
			else:
				await message.answer(text="Вы не можете ввести новый никнейм, пока идет прошлый поиск ! ",reply_markup = LoginSearch)



	else:
		await message.answer(text="""Зарегистрируйтесь !""",reply_markup = registration)



##############################################################################################################################################################################
    







	
    
    