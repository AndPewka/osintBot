import sqlite3
import datetime
###############################################################################################################################################
def create_base_person():
	con = sqlite3.connect("baseTelegram.dp")#создаем базу
	cur = con.cursor()#создаем курсор
	cur.execute("""CREATE TABLE IF NOT EXISTS profile(tele_number TEXT,
													  id 		  TEXT,
													  first_name  TEXT,
													  last_name   TEXT)""")#создаем таблицу со столбцами name и age
	con.commit() # сохраняем изменения таблицы НЕ ЗАБЫВАТЬ ЭТО ПИСАТЬ
	cur.close()#отменяем курсор в таблицу
	con.close()#закрываем таблицу

def trial_to_reg(user_id):
	description = []
	description.append(user_id)
	con = sqlite3.connect("baseTelegram.dp")#создаем базу
	cur = con.cursor()#создаем курсор
	cur.execute("DELETE FROM profile WHERE id = ?",description)
	cur.execute("DELETE FROM bomber WHERE id = ?",description)
	cur.execute("DELETE FROM search WHERE id = ?",description)
	cur.execute("DELETE FROM flag WHERE id = ?",description)
	con.commit() # сохраняем изменения таблицы НЕ ЗАБЫВАТЬ ЭТО ПИСАТЬ
	cur.close()
	con.close()

def base_regisrt(phone_number,user_id,name,last_name):
	description=[]
	con = sqlite3.connect("baseTelegram.dp")#создаем базу
	cur = con.cursor()#создаем курсор
	description.append(phone_number)
	description.append(user_id)
	description.append(name)
	description.append(last_name)

	cur.execute("INSERT INTO profile VALUES(?,?,?,?)",description)
	con.commit()
	cur.close()
	con.close()
	del description


	description=[]
	description.append(user_id)
	description.append("?")
	description.append("0")
	con = sqlite3.connect("baseTelegram.dp")#создаем базу
	cur = con.cursor()#создаем курсор
	cur.execute("INSERT INTO bomber VALUES(?,?,?)",description)
	con.commit() # сохраняем изменения таблицы НЕ ЗАБЫВАТЬ ЭТО ПИСАТЬ
	cur.close()#отменяем курсор в таблицу
	con.close()#закрываем таблицу
	del description

	description=[]
	description.append(user_id)
	description.append("?")
	con = sqlite3.connect("baseTelegram.dp")#создаем базу
	cur = con.cursor()#создаем курсор
	cur.execute("INSERT INTO search VALUES(?,?)",description)
	con.commit() # сохраняем изменения таблицы НЕ ЗАБЫВАТЬ ЭТО ПИСАТЬ
	cur.close()#отменяем курсор в таблицу
	con.close()#закрываем таблицу
	del description

	description=[]
	description.append(user_id)
	description.append("0")
	description.append("0")
	description.append("0")
	description.append("0")
	description.append("0")
	con = sqlite3.connect("baseTelegram.dp")#создаем базу
	cur = con.cursor()#создаем курсор
	cur.execute("INSERT INTO flag VALUES(?,?,?,?,?,?)",description)
	con.commit() # сохраняем изменения таблицы НЕ ЗАБЫВАТЬ ЭТО ПИСАТЬ
	cur.close()#отменяем курсор в таблицу
	con.close()#закрываем таблицу
	del description

	description=[]
	description.append(0)
	description.append(0)
	description.append(0)
	con = sqlite3.connect("baseTelegram.dp")#создаем базу
	cur = con.cursor()#создаем курсор
	cur.execute("INSERT INTO statistics VALUES(?,?,?)",description)
	con.commit() # сохраняем изменения таблицы НЕ ЗАБЫВАТЬ ЭТО ПИСАТЬ
	cur.close()#отменяем курсор в таблицу
	con.close()#закрываем таблицу
	del description


def check_registr(user_id):
	
	con = sqlite3.connect("baseTelegram.dp")#создаем базу
	cur = con.cursor()#создаем курсор
	cur.execute("SELECT id from profile")
	data = cur.fetchall()

	for i in range(len(data)):
		description = []
		description.append(user_id)
		cur.execute("SELECT first_name,last_name from profile WHERE id = ?",description)
		dp = cur.fetchall()
		if dp != []:
			first_name = dp[0][0]
			last_name = dp[0][1]
			del description

			if first_name != "trial":
				return "reg"
			else:

				now = datetime.datetime.now()
				now = str(now.date())
				if str(last_name) == now:
					return "trial"
				else:
					return "trial_time"
		else:
			return "not reg"

	cur.close()
	con.close()

###############################################################################################################################################
def create_bomber_target():
	con = sqlite3.connect("baseTelegram.dp")#создаем базу
	cur = con.cursor()#создаем курсор
	cur.execute("""CREATE TABLE IF NOT EXISTS bomber(id          TEXT,
													 target_sms  TEXT,
													 count_sms   TEXT)""")
	con.commit() # сохраняем изменения таблицы НЕ ЗАБЫВАТЬ ЭТО ПИСАТЬ
	cur.close()#отменяем курсор в таблицу
	con.close()#закрываем таблицу

def update_bomber_target(user_id,mess,lake):
	description=[]
	con = sqlite3.connect("baseTelegram.dp")#создаем базу
	cur = con.cursor()#создаем курсор
	description.append(mess)
	description.append(user_id)

	if lake == 0:
		cur.execute("UPDATE bomber SET target_sms = ? WHERE id = ?",description)
	else:
		cur.execute("UPDATE bomber SET count_sms = ? WHERE id = ?",description)

	con.commit() # сохраняем изменения таблицы НЕ ЗАБЫВАТЬ ЭТО ПИСАТЬ
	cur.close()#отменяем курсор в таблицу
	con.close()#закрываем таблицу
	del description

def check_bomber_target(user_id):
	con = sqlite3.connect("baseTelegram.dp")#создаем базу
	description =[]
	description.append(user_id)
	cur = con.cursor()#создаем курсор
	cur.execute('SELECT target_sms,count_sms from bomber WHERE id = ?',description)#создаем таблицу со столбцами name и age
	messange = cur.fetchall()
	con.commit() # сохраняем изменения таблицы НЕ ЗАБЫВАТЬ ЭТО ПИСАТЬ
	cur.close()#отменяем курсор в таблицу
	con.close()#закрываем таблицу
	del description
	return messange
###############################################################################################################################################
def create_target_Search():
	con = sqlite3.connect("baseTelegram.dp")#создаем базу
	cur = con.cursor()#создаем курсор
	cur.execute("""CREATE TABLE IF NOT EXISTS search(id           TEXT,
													 target_name  TEXT)""")
	con.commit() # сохраняем изменения таблицы НЕ ЗАБЫВАТЬ ЭТО ПИСАТЬ
	cur.close()#отменяем курсор в таблицу
	con.close()#закрываем таблицу

def update_search_target(user_id,mess):
	description=[]
	con = sqlite3.connect("baseTelegram.dp")#создаем базу
	cur = con.cursor()#создаем курсор
	description.append(mess)
	description.append(user_id)

	cur.execute("UPDATE search SET target_name = ? WHERE id = ?",description)


	con.commit() # сохраняем изменения таблицы НЕ ЗАБЫВАТЬ ЭТО ПИСАТЬ
	cur.close()#отменяем курсор в таблицу
	con.close()#закрываем таблицу
	del description

def check_search_target(user_id):
	con = sqlite3.connect("baseTelegram.dp")#создаем базу
	description =[]
	description.append(user_id)
	cur = con.cursor()#создаем курсор
	cur.execute('SELECT target_name from search WHERE id = ?',description)#создаем таблицу со столбцами name и age
	messange = cur.fetchall()
	con.commit() # сохраняем изменения таблицы НЕ ЗАБЫВАТЬ ЭТО ПИСАТЬ
	cur.close()#отменяем курсор в таблицу
	con.close()#закрываем таблицу
	del description
	return messange[0][0]
###############################################################################################################################################

###############################################################################################################################################

def create_flag():
	con = sqlite3.connect("baseTelegram.dp")#создаем базу
	cur = con.cursor()#создаем курсор
	cur.execute("""CREATE TABLE IF NOT EXISTS flag(id             TEXT,
												   PhoneInfo      TEXT,
												   LoginSearch    TEXT,
												   PhoneSpam      TEXT,
												   is_PhoneSpam   TEXT,
												   is_LoginSearch TEXT)""")
	con.commit() # сохраняем изменения таблицы НЕ ЗАБЫВАТЬ ЭТО ПИСАТЬ
	cur.close()#отменяем курсор в таблицу
	con.close()#закрываем таблицу

def update_flag(user_id,mess,number):
	description=[]
	con = sqlite3.connect("baseTelegram.dp")#создаем базу
	cur = con.cursor()#создаем курсор
	description.append(mess)
	description.append(user_id)
	if number == 1:
		cur.execute("UPDATE flag SET PhoneInfo = ? WHERE id = ?",description)
	elif number == 2:
		cur.execute("UPDATE flag SET LoginSearch = ? WHERE id = ?",description)
	elif number == 3:
		cur.execute("UPDATE flag SET PhoneSpam = ? WHERE id = ?",description)
	elif number == 4:
		cur.execute("UPDATE flag SET is_PhoneSpam = ? WHERE id = ?",description)
	elif number == 5:
		cur.execute("UPDATE flag SET is_LoginSearch = ? WHERE id = ?",description)

	con.commit() # сохраняем изменения таблицы НЕ ЗАБЫВАТЬ ЭТО ПИСАТЬ
	cur.close()#отменяем курсор в таблицу
	con.close()#закрываем таблицу
	del description

def check_flag(user_id,number):
	con = sqlite3.connect("baseTelegram.dp")#создаем базу
	description =[]
	description.append(user_id)
	cur = con.cursor()#создаем курсор
	if number == 1:
		cur.execute('SELECT PhoneInfo from flag WHERE id = ?',description)#создаем таблицу со столбцами name и age
	elif number == 2:
		cur.execute('SELECT LoginSearch from flag WHERE id = ?',description)#создаем таблицу со столбцами name и age
	elif number == 3:
		cur.execute('SELECT PhoneSpam from flag WHERE id = ?',description)#создаем таблицу со столбцами name и age
	elif number == 4:
		cur.execute('SELECT is_PhoneSpam from flag WHERE id = ?',description)#создаем таблицу со столбцами name и age
	elif number == 5:
		cur.execute('SELECT is_LoginSearch from flag WHERE id = ?',description)#создаем таблицу со столбцами name и age


	messange = cur.fetchall()
	con.commit() # сохраняем изменения таблицы НЕ ЗАБЫВАТЬ ЭТО ПИСАТЬ
	cur.close()#отменяем курсор в таблицу
	con.close()#закрываем таблицу
	del description
	return messange[0][0]
###############################################################################################################################################


def create_statistics():
	con = sqlite3.connect("baseTelegram.dp")#создаем базу
	cur = con.cursor()#создаем курсор
	cur.execute("""CREATE TABLE IF NOT EXISTS statistics(count_get      INTEGER,
												   		 count_sms      INTEGER,
												   		 count_login    INTEGER)""")
	con.commit() # сохраняем изменения таблицы НЕ ЗАБЫВАТЬ ЭТО ПИСАТЬ
	cur.close()#отменяем курсор в таблицу
	con.close()#закрываем таблицу

def update_statistics(number,inc_count = 1):
	description=[]
	con = sqlite3.connect("baseTelegram.dp")#создаем базу
	cur = con.cursor()#создаем курсор
	if number == 1:
		count = get_statistics(1) + inc_count
		description.append(count)
		cur.execute("UPDATE statistics SET count_get = ?",description)
	elif number == 3:
		count = get_statistics(3) + int(inc_count)
		description.append(count)
		cur.execute("UPDATE statistics SET count_sms = ?",description)
	elif number == 4:
		count = get_statistics(4) + inc_count
		description.append(count)
		cur.execute("UPDATE statistics SET count_login = ?",description)

	con.commit() # сохраняем изменения таблицы НЕ ЗАБЫВАТЬ ЭТО ПИСАТЬ
	cur.close()#отменяем курсор в таблицу
	con.close()#закрываем таблицу
	del description

def get_statistics(number):
	con = sqlite3.connect("baseTelegram.dp")#создаем базу
	description =[]
	cur = con.cursor()#создаем курсор
	if number == 1:
		cur.execute('SELECT count_get from statistics',description)#создаем таблицу со столбцами name и age
	elif number == 3:
		cur.execute('SELECT count_sms from statistics',description)#создаем таблицу со столбцами name и age
	elif number == 4:
		cur.execute('SELECT count_login from statistics',description)#создаем таблицу со столбцами name и age


	messange = cur.fetchall()
	con.commit() # сохраняем изменения таблицы НЕ ЗАБЫВАТЬ ЭТО ПИСАТЬ
	cur.close()#отменяем курсор в таблицу
	con.close()#закрываем таблицу
	del description
	return messange[0][0]
###############################################################################################################################################
def get_base(table):
	con = sqlite3.connect("baseTelegram.dp")#создаем базу
	cur = con.cursor()#создаем курсор
	cur.execute("SELECT * from " + table)
	data = cur.fetchall()


	for column in range(len(data)):
		if column>0:
			print("")                                        
		for line in range(len(data[column])):                #
			margin = (25 - len(data[column][line])) * " "    #
			print(data[column][line],end = margin)           #

	cur.close()
	con.close()



create_base_person()
create_bomber_target()
create_target_Search()
create_flag()
create_statistics()

#profile     bomber   search flag
get_base("profile")
#print(check_registr("1164420593"))





