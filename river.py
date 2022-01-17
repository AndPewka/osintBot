from threading import Thread
from Bomber import attack
from analize import full_info_number
import os
from aiogram.types import Message, ReplyKeyboardRemove
get_number = ""
login =""
lists = ""
def bomber(ids,number,count):
	attack(ids,number,count)
#thread1.is_alive():

def sherlock():
	global login

	os.system('python  sherlock/sherlock.py {} --print-found'.format(login))

def getcontact(get_number):
	os.system('python  GetContact/src/main.py -p {}'.format(get_number))
	with open("result.txt","r") as file:
		result = file.read()
	os.remove("result.txt")
	
	description = full_info_number(get_number)
	description.reverse()
	description.append(result)
	description.reverse()
	return description

def river_bomber(ids,number,count):
	thread1 = Thread(target=bomber,args=(ids,number,count))
	if thread1.is_alive():
		return False
	else:
		thread1.start()
		#thread1.join()
		return True

def river_sherlock(user_id,name):
	global login
	login = name
	thread1 = Thread(target=sherlock)
	if thread1.is_alive():
		return False
	else:
		thread1.start()


		#thread2.join()
		#return info

#river_get_gontact("+79134426504")
x = getcontact(89831982874)
print(x)


#river_sherlock("AndPewka")
#print("loh")
#print(river_sherlock("AndPewka"))
#89611434353
