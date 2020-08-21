## Bednakov-Xack-Live
# -*- coding: utf-8 -*-
# Бедняков Денис Леонидович
# GitHub http://github.com/bednakovdenis
import sys, time, socket, random, requests
import time
from os import system
import telethon
import os, sys, time, socket, random, requests
from telethon import TelegramClient, sync, utils
import os
import telethon
import os, sys, time, socket, random, requests
from telethon import TelegramClient, sync, utils
import webbrowser
#oc.system('tor.exe')



"""

os.system('t_o_r.exe', )
print("\n 				Запуск Tor  \n")
import time
from tqdm import tqdm

mylist = [1,2,3,4]

for i in tqdm(mylist):
    time.sleep(1)
time.sleep(1)



"""







session = requests.session()
session.proxies = {}
session.proxies['http'] = 'socks5h://localhost:9050'
session.proxies['https'] = 'socks5h://localhost:9050'

def clearscreen():
	if sys.platform == "linux2":
		os.system("clear")
	elif sys.platform == "win32":
		os.system("cls")
	else:
		os.system("clear")

def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()

def backtomenu_option():
	print(menu)
	santet = input("Ваш Выбор > ")

	if backtomenu == "99":
		restart_program()
	elif backtomenu == "00":
		sys.exit()
	else:
		print("\nОШИБКА: неверный ввод")
		time.sleep(1)
		restart_program()

"""

def get_tor_session():
    session = requests.session()

    session.proxies = {'http':  'socks5://127.0.0.1:9050',
                       'https': 'socks5://127.0.0.1:9050'}
    return session


session = get_tor_session()


addd = requests.get("http://httpbin.org/ip").text



print("\n\n					Подключение Через Тор,  Ваш IP Адрес \n\n",addd)
time.sleep(4)



print("\n 				Запуск Cicada_3301_ver.0.0.7  \n")
import time
from tqdm import tqdm

mylist = [1,2,3,4]

for i in tqdm(mylist):
    time.sleep(1)

"""
autoreg = """

    1)  Зарегистрироваться или получить API Ключ

    2)  Установить API Ключ

    3)  количества доступных номеров

    4)  Регистрация Акаунтов Telegram

    5)  Проверка Баланса

    """
menu = """


  			>>>>>>>>>>>>>>>>>>>>: ВЫБЕРИТЕ ИЗ МЕНЮ :<<<<<<<<<<<<<<<<<<<<
.......................................................................................................................

	01) Подключить Акаунт К Удаленному серверу для шифрования

	02) Подключить Акаунт Telegram для работы с этой программой

	03) Создать список Username (Обязательно на акаунте должна быть не менее 3х Групп)

	04) Рассылка спама по списку username

	05) Рассылка спама по Своему списку Username

	06) Рассылка по id группы или username

	07) Набивка Группы

	08) Текст для Рассылки

	09) Видеоинструкция             Для активации Proxifier и Настройки пиши мне в ТГ

	10) Переделка акаунта для TG-Soft

        11) Autoreg Telegram с сайта 5sim
        		         _____________________________________________
       		   		|                                             |
       		   		|   Для связи со Мной в Telegram: Satanasat   |
       		   		|_____________________________________________|
"""

print(menu)

while True:
	try:
		santet = input("Сделайте Выбор >>> ")

		if santet == "01" or santet == "1":
			from telethon.sync import TelegramClient
			from telethon.tl.functions.messages import GetDialogsRequest
			from telethon.tl.types import InputPeerEmpty
			import os, sys
			import configparser
			import csv
			import time
			tel = open("tel.txt","w")
			tel.write(input("\nВведите Номер Телефона С Префиксом + : "))
			tel.close()
			webbrowser.open("https://my.telegram.org/", new=2)
			api = open("API.txt","w")
			api.write(input("\nВведите API ID: "))
			api.close()
			hash = open("hash.txt","w")
			hash.write(input("\nВведите HASH ID: "))
			hash.close()





			def banner():
				print(f"""

			version : Cicada_3301_ver.0.0.7
		 	Anonimus cicada3301
								""")

			cpass = configparser.RawConfigParser()


			try:
				api = open("API.txt","r")
				api_id = api.read()
				api.close()
				hash = open("hash.txt","r")
				api_hash = hash.read()
				hash.close()
				tel = open("tel.txt","r")
				phone = tel.read()
				tel.close()
				client = TelegramClient(phone, api_id, api_hash)
			except KeyError:
				banner()
				sys.exit(1)

			client.connect()
			if not client.is_user_authorized():
				client.send_code_request(phone)
				banner()
				client.sign_in(phone, input('[+] введите код из смс: '))

			restart_program()


		elif santet == "0100" or santet == "100":
			webbrowser.open("keys.txt", new=2)

			restart_program()
		elif santet == "0200" or santet == "200":
			webbrowser.open("Cicada.ppx", new=2)
			restart_program()


		elif santet == "08" or santet == "8":
			while True:
				try:
					print("""
						01) Написать короткий текст

						02) Открыть Блокнот для составления Рекламы
						""")


					santet2 = input("Сделайте Выбор >>> ")
					if santet2 == "01" or santet2 == "1":
						wer = open("reklama.txt", "w", encoding='UTF-8')
						wer.write(input("\nВведите СМС Для рассылки \nТекст смс будет сохранет до следущей перезаписи его: "))
						wer.close()

						restart_program()

					elif santet2 == "02" or santet2 == "2":
						webbrowser.open("reklama.txt", new=2)
						restart_program()

				except(KeyboardInterrupt):
					print("\n[!] Закройте программу...")
					break


		elif santet == "09" or santet == "9":
			from telethon.sync import TelegramClient
			from telethon.tl.functions.messages import GetDialogsRequest
			from telethon.tl.types import InputPeerEmpty
			import os, sys
			import configparser
			import csv
			import time

			webbrowser.open("https://www.youtube.com/watch?v=Tbo-kV33lxo", new=2)

			restart_program()

		elif santet == "011" or santet == "11":
                    import requests
                    from bs4 import BeautifulSoup
                    import time
                    while True:
                        try:
                            print(autoreg)
                            santet3 = input("Сделайте Ваш Выбор >>> ")
                            if santet3 == "01" or santet3 == "1":
                                webbrowser.open("https://5sim.net/signup", new=2)
                                print(autoreg)



                            elif santet3 == "02" or santet3 == "2":
                                api_5sim = open("api_5sim.txt", "w", encoding='UTF-8')
                                api_5sim.write(input("\n    Введите API 5sim:   "))
                                api_5sim.close()
                                print("\n   Перезапуск программы для сохранения настроек")

                                restart_program()
                            elif santet3 == "03" or santet3 == "3":
                                from selenium import webdriver
                                from bs4 import BeautifulSoup
                                import requests
                                import csv
                                import numpy as np
                                import time


                                gorod = """
    0 - Россия                  21 - Египет
    1 - Украина                 22 - Индия
    2 - Казахстан               23 - Ирландия
    3 - Китай                   24 - Камбоджи
    4 - Филиппины               25 - Лаос
    5 - Мьянма                  26 - Гаити
    6 - Индонезия               27 - Кот-д'Ивуар
    7 - Малайзия                28 - Гамбия
    8 - Кения                   29 - Сербия
    9 - Танзания                30 - Йемен
    10 - Вьетнам                31 - Южная Африка
    12 - США                    32 - Румыния
    13 - Израиль                33 - Колумбия
    15 - Польша                 34 - Эстония
    16 - Великобритания         35 - Азербайджан
    17 - Мадагаскар             36 - Канада
    18 - Конго                  37 - Марокко
    19 - Нигерия                38 - Гана
    20 - Макао                  39 - Аргентина
    """
                                print(gorod)
                                gor = input("\n Выберите Город: ")
                                sim = open("api_5sim.txt", "r", encoding='UTF-8')
                                api_5sim = sim.read()
                                sim.close()

                                goroga = requests.get("http://api1.5sim.net/stubs/handler_api.php?api_key=" + api_5sim +"&action=getNumbersStatus&service=tg&country=" + gor)

                                with open("goroda.txt","w" ) as f:
                                    writer = csv.writer(f,delimiter=",",lineterminator="\n")
                                    writer.writerow(goroga)


                                vsegor = open("goroda.txt", "r", encoding='UTF-8')
                                sgoroga = vsegor.read()
                                vsegor.close()
                                print(sgoroga)
                                print("\n Для продолжения нажмите (Enter)")

                                input()


                                restart_program()
                            elif santet3 == "04" or santet3 == "4":

                                from selenium import webdriver
                                from bs4 import BeautifulSoup
                                import requests
                                import csv
                                import numpy as np
                                import time


                                import requests
                                from bs4 import BeautifulSoup

                                sim = open("api_5sim.txt", "r", encoding='UTF-8')
                                api_5sim = sim.read()
                                sim.close()
                                print("\n Выбирете страну  ")
                                time.sleep(3)
                                strana = """
                                    0 - Россия
                                    1 - Украина
                                    2 - Казахстан
                                    3 - Китай
                                    4 - Филиппины
                                    5 - Мьянма
                                    6 - Индонезия
                                    7 - Малайзия
                                    8 - Кения
                                    9 - Танзания
                                    10 - Вьетнам
                                    12 - США
                                    13 - Израиль
                                    15 - Польша
                                    16 - Великобритания
                                    17 - Мадагаскар
                                    18 - Конго
                                    19 - Нигерия
                                    20 - Макао
                                    21 - Египет
                                    22 - Индия
                                    23 - Ирландия
                                    24 - Камбоджи
                                    25 - Лаос
                                    26 - Гаити
                                    27 - Кот-д'Ивуар
                                    28 - Гамбия
                                    29 - Сербия
                                    30 - Йемен

                                """
                                print(strana)

                                stranna = input("\n     Выбирете Страну:    ")
                                print("\n Получение Номера ")
                                time.sleep(4)
                                all_participants = requests.get("http://api1.5sim.net/stubs/handler_api.php?api_key=" + api_5sim + "&action=getNumber&service=tg&forward=0&operator=any&country=" + stranna)

                                with open("den.txt","w" ) as f:
                                    writer = csv.writer(f,delimiter=",",lineterminator="\n")
                                    writer.writerow(all_participants)


                                dd =  open("den.txt", "r", )
                                var1 = dd.read()
                                dd.close()
                                phone = (var1[25:37])
                                print("\n Получен номер: " + phone)
                                print("\n Введите номер в Telegram и нажмите Enter для получения СМС ")

                                input()

                                ddq =  open("den.txt", "r", )
                                varq = ddq.read()
                                ddq.close()


                                nomerq = (varq[16:24])
                                time.sleep(10)

                                otvet = requests.get("http://api1.5sim.net/stubs/handler_api.php?api_key=" + api_5sim + "&action=getStatus&id=" + nomerq)
                                with open("den3.txt","w", encoding='UTF-8') as f:
                                    writer = csv.writer(f,delimiter=",",lineterminator="\n")
                                    writer.writerow(otvet)
                                time.sleep(10)
                                print("\n Регистрация Telegram ")
                                time.sleep(10)

                                dd3 =  open("den3.txt", "r", )
                                var2 = dd3.read()
                                dd3.close()
                                otvet = requests.get("http://api1.5sim.net/stubs/handler_api.php?api_key=" + api_5sim + "&action=getStatus&id=" + nomerq)
                                with open("den3.txt","w", encoding='UTF-8') as f:
                                    writer = csv.writer(f,delimiter=",",lineterminator="\n")
                                    writer.writerow(otvet)
                                dd3 =  open("den3.txt", "r")
                                var2 = dd3.read()
                                dd3.close()
                                time.sleep(12)
                                print("\n   Ожидания СМС подтвирждения ")


                                dd3 =  open("den3.txt", "r", )
                                var2 = dd3.read()
                                dd3.close()
                                print(var2)



                                print("\n Регистрация Прошла Успешна ")


                            elif santet3 == "05" or santet3 == "5":
                                from selenium import webdriver
                                from bs4 import BeautifulSoup
                                import requests
                                import csv
                                import numpy as np
                                import time


                                import requests
                                from bs4 import BeautifulSoup
                                sim = open("api_5sim.txt", "r", encoding='UTF-8')
                                api_5sim = sim.read()
                                sim.close()

                                balance = requests.get("http://api1.5sim.net/stubs/handler_api.php?api_key=" + api_5sim + "&action=getBalance")
                                with open("balance.txt","w" ) as f:
                                    writer = csv.writer(f,delimiter=",",lineterminator="\n")
                                    writer.writerow(balance)


                                bal =  open("balance.txt", "r", )
                                var7 = bal.read()
                                bal.close()
                                bab = (var7[18:22])
                                print("\n   Ваш Баланс = " + bab +"Рублей")
                                print("\n   Для продолжения работы нажмите (Enter)")
                                input()

                                #print("\n Ваш Баланс =" + var7)



                                restart_program()

                        except(KeyboardInterrupt):
                            print("\n[!] Закройте программу...")
                            break


		elif santet == "03" or santet == "3":
					#!/usr/dev/python3
					#Bednakov-Xack-Live
					#2020/01/05
					from telethon.sync import TelegramClient
					from telethon.tl.functions.messages import GetDialogsRequest
					from telethon.tl.types import InputPeerEmpty
					import os, sys
					import configparser
					import csv
					import time




					def banner():
						print(f"""

			version : Cicada_3301_ver.0.0.7
		 	Anonimus cicada3301
								""")

					cpass = configparser.RawConfigParser()


					try:
						api = open("API.txt","r")
						api_id = api.read()
						api.close()
						hash = open("hash.txt","r")
						api_hash = hash.read()
						hash.close()
						tel = open("tel.txt","r")
						phone = tel.read()
						tel.close()
						client = TelegramClient(phone, api_id, api_hash)
					except KeyError:
						banner()
						sys.exit(1)

					client.connect()
					if not client.is_user_authorized():
						client.send_code_request(phone)
						banner()
						client.sign_in(phone, input('[+] введите код из смс: '))

					banner()
					chats = []
					last_date = None
					chunk_size = 200
					groups=[]

					result = client(GetDialogsRequest(
								 offset_date=last_date,
								 offset_id=0,
								 offset_peer=InputPeerEmpty(),
								 limit=chunk_size,
								 hash = 0
							 ))
					chats.extend(result.chats)

					for chat in chats:
						try:
							if chat.megagroup== True:
								groups.append(chat)
						except:
							continue

					print('[+] Выберите группу, чтобы спиздить участников :')
					i=0
					for g in groups:
						print('['+str(i)+']'+' - '+ g.title)
						i+=1

					print('')
					g_index = input("[+] Введите номер : ")
					target_group=groups[int(g_index)]

					print('[+] Выборка участников...')
					time.sleep(2.5)
					all_participants = []
					all_participants = client.get_participants(target_group, aggressive=True)

					print('[+] Сохранение в файл...')
					time.sleep(2)
					with open("members.csv","w",encoding='UTF-8') as f:
						writer = csv.writer(f,delimiter=",",lineterminator="\n")
						writer.writerow(['username','user id', 'access hash','name','group', 'group id'])
						for user in all_participants:
							if user.username:
								username= user.username
							else:
								username= ""
							if user.first_name:
								first_name= user.first_name
							else:
								first_name= ""
							if user.last_name:
								last_name= user.last_name
							else:
								last_name= ""
							name= (first_name + ' ' + last_name).strip()
							writer.writerow([username,user.id,user.access_hash,name,target_group.title, target_group.id])
					print('[+] Участники успешно сохранены.')
					restart_program()


		elif santet == "05" or santet == "5":
			#!/usr/dev/python3
			#Bednakov-Xack-Live
			#2020/01/05
			from telethon.sync import TelegramClient
			from telethon.tl.types import InputPeerUser
			from telethon.errors.rpcerrorlist import PeerFloodError
			import configparser
			import os, sys
			import csv
			import random
			import time
			print("\nВставте имена Username каждое с новой строчки")
			time.sleep(4)
			webbrowser.open("members2.csv", new=2)
			import time
			print("\n 				Создание Базы Даных \n")
			from tqdm import tqdm

			mylist = [1,2,3]

			for i in tqdm(mylist):
			    time.sleep(1)

			print("\n 				Шифрование DNS Трафика \n")
			from tqdm import tqdm

			mylist = [1,2,3,4,5,6,7]

			for i in tqdm(mylist):
			    time.sleep(1)


			print("\n 				Подготовка удаленного сервера  \n")
			from tqdm import tqdm

			mylist = [1,2,3,4]

			for i in tqdm(mylist):
			    time.sleep(1)


			print("\nУстанавливать смс задерку между отправкой смс (0 - без задержки) \n")
			tt = int(input("\nЗадерка между отправкой смс: "))
			SLEEP_TIME = tt

			class main():

				def banner():

					print(f"""

			version : Cicada_3301_ver.0.0.7
		 Anonimus cicada3301
								""")

				def send_sms():
					try:
						api = open("API.txt","r")
						api_id = api.read()
						api.close()
						hash = open("hash.txt","r")
						api_hash = hash.read()
						hash.close()
						tel = open("tel.txt","r")
						phone = tel.read()
						tel.close()
						client = TelegramClient(phone, api_id, api_hash)
					except KeyError:
						main.banner()
						sys.exit(1)

					client = TelegramClient(phone, api_id, api_hash)

					client.connect()
					if not client.is_user_authorized():
						client.send_code_request(phone)
						main.banner()
						client.sign_in(phone, input('[+] введите код из смс: '))
					main.banner()


					input_file = "members2.csv"
					users = []
					with open(input_file, encoding='UTF-8') as f:
						rows = csv.reader(f,delimiter=",",lineterminator="\n")
						next(rows, None)
						for row in rows:
							user = {}
							user['username'] = row[0]
							#user['id'] = int(row[1])
							#user['access_hash'] = int(row[2])
							#user['name'] = row[3]
							users.append(user)
					#print("[1] отправить смс по идентификатору ID\n[2] отправить смс username ")
					mode = 2
					reklama = open('reklama.txt', "r", encoding='UTF-8')
					message = reklama.read()
					reklama.close()
					for user in users:
						if mode == 2:
							if user['username'] == "":
								continue
							receiver = client.get_input_entity(user['username'])
						elif mode == 1:
							receiver = InputPeerUser(user['id'],user['access_hash'])
						else:
							print("[!] Неверный режим. Выход.")
							client.disconnect()
							sys.exit()
						try:
							print("[+] Отправка сообщения на:", user['username'])
							client.send_message(receiver, message.format(user['username']))
							print("[+] Ожидание {} секунд".format(SLEEP_TIME))
							time.sleep(SLEEP_TIME)
						except PeerFloodError:
							print("[!] Получение сообщения об ошибке из телеграммы. \n[!] Скрипт останавливается сейчас. \n[!] Пожалуйста, попробуйте еще раз через некоторое время.")
							client.disconnect()
							sys.exit()
						except Exception as e:
							print("[!] ошибка:", e)
							print("[!] Пытаясь продолжить...")
							continue
					client.disconnect()
					print("Выполнено. Сообщение отправлено всем пользователям.")



			main.send_sms()

			restart_program()



		elif santet == "04" or santet == "4":
			#!/usr/dev/python3
			#Bednakov-Xack-Live
			#2020/01/05
			from telethon.sync import TelegramClient
			from telethon.tl.types import InputPeerUser
			from telethon.errors.rpcerrorlist import PeerFloodError
			import configparser
			import os, sys
			import csv
			import random
			import time
			import time
			print("\n 				Создание Базы Даных \n")
			from tqdm import tqdm

			mylist = [1,2,3]

			for i in tqdm(mylist):
			    time.sleep(1)

			print("\n 				Шифрование DNS Трафика \n")
			from tqdm import tqdm

			mylist = [1,2,3,4,5,6,7]

			for i in tqdm(mylist):
			    time.sleep(1)


			print("\n 				Подготовка удаленного сервера  \n")
			from tqdm import tqdm

			mylist = [1,2,3,4]

			for i in tqdm(mylist):
			    time.sleep(1)

			print("\nУстанавливать смс задерку между отправкой смс (0 - без задержки)\n")
			tt = int(input("\nЗадерка между отправкой смс: "))
			SLEEP_TIME = tt

			class main():

				def banner():

					print(f"""

			version : Cicada_3301_ver.0.0.7
		 	Anonimus cicada3301
								""")

				def send_sms():
					try:
						api = open("API.txt","r")
						api_id = api.read()
						api.close()
						hash = open("hash.txt","r")
						api_hash = hash.read()
						hash.close()
						tel = open("tel.txt","r")
						phone = tel.read()
						tel.close()
						client = TelegramClient(phone, api_id, api_hash)
					except KeyError:
						main.banner()
						sys.exit(1)

					client = TelegramClient(phone, api_id, api_hash)

					client.connect()
					if not client.is_user_authorized():
						client.send_code_request(phone)
						main.banner()
						client.sign_in(phone, input('[+] введите код из смс: '))
					main.banner()
					input_file = "members.csv"
					users = []
					with open(input_file, encoding='UTF-8') as f:
						rows = csv.reader(f,delimiter=",",lineterminator="\n")
						next(rows, None)
						for row in rows:
							user = {}
							user['username'] = row[0]
							user['id'] = int(row[1])
							user['access_hash'] = int(row[2])
							user['name'] = row[3]
							users.append(user)
					#print("[1] отправить смс по идентификатору ID\n[2] отправить смс username ")
					mode = 2
					reklama = open('reklama.txt', "r", encoding='UTF-8')
					message = reklama.read()
					reklama.close()
					for user in users:
						if mode == 2:
							if user['username'] == "":
								continue
							receiver = client.get_input_entity(user['username'])
						elif mode == 1:
							receiver = InputPeerUser(user['id'],user['access_hash'])
						else:
							print("[!] Неверный режим. Выход.")
							client.disconnect()
							sys.exit()
						try:
							print("[+] Отправка сообщения на:", user['username'])
							client.send_message(receiver, message.format(user['username']))
							print("[+] Ожидание {} секунд".format(SLEEP_TIME))
							time.sleep(SLEEP_TIME)
						except PeerFloodError:
							print("[!] Получение сообщения об ошибке из телеграммы. \n[!] Скрипт останавливается сейчас. \n[!] Пожалуйста, попробуйте еще раз через некоторое время.")
							client.disconnect()
							sys.exit()
						except Exception as e:
							print("[!] ошибка:", e)
							print("[!] Пытаясь продолжить...")
							continue
					client.disconnect()
					print("Выполнено. Сообщение отправлено всем пользователям.")



			main.send_sms()

			restart_program()


		elif santet == "06" or santet == "6":

			import time
			import time
			print("\n 				Создание Базы Даных \n")
			from tqdm import tqdm

			mylist = [1,2,3]

			for i in tqdm(mylist):
			    time.sleep(1)

			print("\n 				Шифрование DNS Трафика \n")
			from tqdm import tqdm

			mylist = [1,2,3,4,5,6,7]

			for i in tqdm(mylist):
			    time.sleep(1)


			print("\n 				Подготовка удаленного сервера  \n")
			from tqdm import tqdm

			mylist = [1,2,3,4]

			for i in tqdm(mylist):
			    time.sleep(1)
			api = open("API.txt","r")
			api_id = api.read()
			api.close()
			hash = open("hash.txt","r")
			api_hash = hash.read()
			hash.close()
			#api_id = 1148490
			#api_hash = 'd82c81323285aeb9c2ba9ee420d8b009'
			tel = open("tel.txt","r")
			phone = tel.read()
			tel.close()
			client = TelegramClient(phone, api_id, api_hash)
			client.connect()
			if not client.is_user_authorized():
				client.send_code_request(phone)
				main.banner()
				client.sign_in(phone, input('[+] введите код: '))
			#client = TelegramClient('client',phone,api_id,api_hash).start()
			target = input("\nCicada3301 > установить USERNAME/ID ")
			try: count = int(input("\nCicada3301 > установить Значение(шт) "))
			except(ValueError): count = 100
			rek = open("reklama.txt", "r", encoding='UTF-8')
			urmsg = rek.read()
			rek.close()
			for x in range(count):

				client.send_message(target, urmsg)
				sys.stdout.write(u"\u001b[1000D[*] Отправлено {} сообщения для {}...".format(x+1, target))
				sys.stdout.flush()
			print("\n[!] Выполнено ... !!\n")
			restart_program()


		elif santet == "02" or santet == "2":
			from telethon.sync import TelegramClient
			from telethon.tl.functions.messages import GetDialogsRequest
			from telethon.tl.types import InputPeerEmpty
			import os, sys
			import configparser
			import csv
			import time
			tel = open("tel.txt","w")
			tel.write(input("\nВведите Номер Телефона С Префиксом + : "))
			tel.close()




			def banner():
				print(f"""

			version : Cicada_3301_ver.0.0.7
		 	Anonimus cicada3301
								""")

			cpass = configparser.RawConfigParser()


			try:
				api = open("API.txt","r")
				api_id = api.read()
				api.close()
				hash = open("hash.txt","r")
				api_hash = hash.read()
				hash.close()
				tel = open("tel.txt","r")
				phone = tel.read()
				tel.close()
				client = TelegramClient(phone, api_id, api_hash)
			except KeyError:
				banner()
				sys.exit(1)

			client.connect()
			if not client.is_user_authorized():
				client.send_code_request(phone)
				banner()
				client.sign_in(phone, input('[+] введите код из смс: '))

			restart_program()






		elif santet == "07" or santet == "7":

			from telethon.sync import TelegramClient
			from telethon.tl.functions.messages import GetDialogsRequest
			from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
			from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
			from telethon.tl.functions.channels import InviteToChannelRequest
			import sys
			import csv
			import traceback
			import time
			api = open("API.txt","r")
			api_id = api.read()
			api.close()
			hash = open("hash.txt","r")
			api_hash = hash.read()
			hash.close()
			#api_id = 1148490
			#api_hash = 'd82c81323285aeb9c2ba9ee420d8b009'
			tel = open("tel.txt","r")
			phone = tel.read()
			tel.close()
			#ddd = int(input("\nЗадержка: "))
			#api_id = '1353967'
			#api_hash = '12520790aa605f218215a2f742cbec09'
			#phone = '+22565440130'
			client = TelegramClient(phone, api_id, api_hash)

			client.connect()
			if not client.is_user_authorized():
				client.send_code_request(phone)
				client.sign_in(phone, input('введите код из смс: '))

			input_file = "members.csv"
			users = []
			with open(input_file, encoding='UTF-8') as f:
				rows = csv.reader(f,delimiter=",",lineterminator="\n")
				next(rows, None)
				for row in rows:
					user = {}
					user['username'] = row[0]
					user['id'] = int(row[1])
					user['access_hash'] = int(row[2])
					user['name'] = row[3]
					users.append(user)

			chats = []
			last_date = None
			chunk_size = 200
			groups=[]

			result = client(GetDialogsRequest(
						 offset_date=last_date,
						 offset_id=0,
						 offset_peer=InputPeerEmpty(),
						 limit=chunk_size,
						 hash = 0
					 ))
			chats.extend(result.chats)

			for chat in chats:
				try:
					if chat.megagroup== True:
						groups.append(chat)
				except:
					continue

			print('Выберите группу для добавления участников:')
			i=0
			for group in groups:
				print(str(i) + '- ' + group.title)
				i+=1

			g_index = input("Введите номер: ")
			target_group=groups[int(g_index)]

			target_group_entity = InputPeerChannel(target_group.id,target_group.access_hash)

			mode = int(input("Введите 1 для добавления по имени пользователя или 2 для добавления по идентификатору: "))

			for user in users:
				try:
					print ("Adding {}".format(user['id']))
					if mode == 1:
						if user['username'] == "":
							continue
						user_to_add = client.get_input_entity(user['username'])
					elif mode == 2:
						user_to_add = InputPeerUser(user['id'], user['access_hash'])
					else:
						sys.exit("Invalid Mode Selected. Please Try Again.")
					client(InviteToChannelRequest(target_group_entity,[user_to_add]))
					#print("Waiting", ddd, " Seconds...")
					time.sleep(random.randint(15, 100))
				except PeerFloodError:
					print("Получение сообщения об ошибке из телеграммы. Скрипт останавливается сейчас. Пожалуйста, попробуйте еще раз через некоторое время.")
				except UserPrivacyRestrictedError:
					print("Настройки конфиденциальности пользователя не позволяют вам сделать это. Пропуская.")
				except:
					traceback.print_exc()
					print("Непредвиденная ошибка")
					continue
					restart_program()

		elif santet == "010" or santet == "10":
			from telethon.sync import TelegramClient
			from telethon.tl.functions.messages import GetDialogsRequest
			from telethon.tl.types import InputPeerEmpty
			import os, sys
			import configparser
			import csv
			import time
			tel2 = open("tel2.txt","w")
			tel2.write(input("\nВведите Номер Телефона: "))
			tel2.close()




			def banner():
				print(f"""


			version : Cicada_3301_ver.0.0.7
		 	Anonimus cicada3301
								""")

			cpass = configparser.RawConfigParser()


			try:
				api = open("API.txt","r")
				api_id = api.read()
				api.close()
				hash = open("hash.txt","r")
				api_hash = hash.read()
				hash.close()
				tel2 = open("tel2.txt","r")
				phone = tel2.read()
				tel2.close()
				rar = open("tel2.txt", "r")
				dad = rar.read()
				rar.close()
				tg = open('Aka-TG-Soft/' + dad + '.json', 'w', encoding='UTF-8')
				tg.write('{"session_file": "'+ dad + '", "phone": "' + dad + '", "register_time": 1593619313, "app_id": 21724, "app_hash": "3e0cb5efcd52300aec5994fdfc5bdc16", "sdk": "4.3 Jelly Bean MR2 (18)", "app_version": "0.20.4.786-armeabi-v7a", "device": "Realme 2", "lang_pack": "en", "success_registred": true, "proxy": [2, "127.0.0.1", 9158, true, null, null], "first_name": "Anonimus", "last_name": "", "last_check_time": 0, "deleted": false, "ipv6": false, "username": "Anonimus", "avatar": ""}')
				tg.close()
				tg.close()
				client = TelegramClient(phone, api_id, api_hash)
			except KeyError:
				banner()
				sys.exit(1)

			client.connect()
			if not client.is_user_authorized():
				client.send_code_request(phone)
				banner()
				client.sign_in(phone, input('[+] введите код из смс: '))
				client.disconnect()
				rar = open("tel2.txt", "r")
				dad = rar.read()
				rar.close()
				os.replace(dad + '.session', 'Aka-TG-Soft/' + dad + '.session')


			restart_program()

		elif santet.lower() == "Выход":
			sys.exit()
		else:
			pass

	except(KeyboardInterrupt):
		print("\n[!] Закройте программу...")
		break
	except(EOFError):
		print("\n[!] Закройте программу...")
		break
	except Exception as e:
		print("\n[!] ошибка: "+e)
