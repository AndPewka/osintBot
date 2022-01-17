import sqlite3

def get_id():
	massive_id =[]
	con = sqlite3.connect("baseTelegram.dp")#создаем базу
	cur = con.cursor()#создаем курсор
	cur.execute("SELECT * from flag")
	data = cur.fetchall()
	for i in range(len(data)):
		massive_id.append(data[i][0])
	return	massive_id

	cur.close()
	con.close()

def null_flag():
	massive_id = get_id()
	con = sqlite3.connect("baseTelegram.dp")#создаем базу
	cur = con.cursor()#создаем курсор

	for ids in massive_id:
		description = []
		description.append("0")
		description.append(ids)

		for i in range(1,6):

			if i == 1:
				cur.execute("UPDATE flag SET PhoneInfo = ? WHERE id = ?",description)
			elif i == 2:
				cur.execute("UPDATE flag SET LoginSearch = ? WHERE id = ?",description)
			elif i == 3:
				cur.execute("UPDATE flag SET PhoneSpam = ? WHERE id = ?",description)
			elif i == 4:
				cur.execute("UPDATE flag SET is_PhoneSpam = ? WHERE id = ?",description)
			elif i == 5:
				cur.execute("UPDATE flag SET is_LoginSearch = ? WHERE id = ?",description)
		del description

	con.commit() # сохраняем изменения таблицы НЕ ЗАБЫВАТЬ ЭТО ПИСАТЬ
	cur.close()#отменяем курсор в таблицу
	con.close()#закрываем таблицу
null_flag()
