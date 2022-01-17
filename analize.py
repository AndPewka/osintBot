import requests
from bs4 import BeautifulSoup
description = []
def analize_phone(number):
	link = requests.get("https://kto-abonent.com/phone/{}".format(number))
	soup = BeautifulSoup(link.text,"lxml")
	soup = list(soup.find("ul",class_ = "breadcrumb"))
	return soup[2].find("a").text


def avito(number):
	description = []
	link = requests.get("https://mirror.bullshit.agency/search_by_phone/{}".format(number))
	soup = BeautifulSoup(link.text,"lxml")
	soup = soup.find_all("a", rel = "nofollow")
	for link in soup:
		description.append("https://mirror.bullshit.agency/" + link.get("href"))
	return	description
def drom(number):
	count = 0
	description = []
	link = requests.get("http://{}.drom.ru".format(number))
	soup = BeautifulSoup(link.text,"lxml")
	while True:
		count += 1
		x = soup.find("a", {"name":str(count)})
		try:
			description.append(x.get("href"))
		except AttributeError:
			break
	return description 


def region(number):
	number = number[1:]
	link = requests.get("https://numbase.ru/{}".format(number))
	soup = BeautifulSoup(link.text,"lxml")
	soup = soup.find("div",class_ = "col-xs-12 relation")
	soup = list(soup.find_all("strong"))
	soup = str(soup[1])
	soup = soup.replace("<strong>","");soup = soup.replace("</strong>","")
	return soup


def full_info_number(number):
	description = []
	description.append(region(number))
	description.append(analize_phone(number))
	description.append(avito(number))
	description.append(drom(number))
	return description

#x = full_info_number("89134439330")
#print(x[3])





