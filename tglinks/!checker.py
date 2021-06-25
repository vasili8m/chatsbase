from telethon import TelegramClient, events, sync
from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest
import json
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

api_id = config.get('Telegram','api_id')
api_hash = config.get('Telegram','api_hash')


class App():
	def __init__(self):
		value_accounts = input("Сколько аккаунтов будем использовать?")
		value_check = str('y') #input("Вы уверены? Y-да, n-нет: ")

		if not value_accounts.isdigit():
			print("Упс... Количество аккаунтов должно быть указано цифрой(цифрами) и быть больше 0.\nПопробуй еще раз.\n\n\n")
			return
		if value_check.lower() == "y":
			self.value_accounts = value_accounts
			self.loadusers(value_accounts)
		else:
			print("\n\n\n")
			return
	def loadusers(self, _range):
		for i in range(int(_range)):
			print('Авторизация в аккаунте №{0}'.format(str(i+1)))
			with TelegramClient('account'+str(i+1), api_id, api_hash) as client:
				pass
		self.loadto_parseds()
	def loadto_parseds(self):
		to_parsed = []
		while True:
			try:
				file = open("input.txt")
				break
			except:
				print("Не найден входной файл")
				input()
				
		text = []
		for i in file:
			if i != "\n":
				text.append(i.replace('\n',''))

		
		for i in text:
			try:to_parsed.append(i.split('joinchat/')[1].split(' ')[0])
				
			except:
				try:to_parsed.append(i.split('t.me/')[1].split(' ')[0])
				
					
		#	except:
		#		try:to_parsed.append(i.split('@')[1].split(' ')[0])
				except:
					pass
		#print(to_parsed) # список приглашений
		self.checker_function(to_parsed)
	def checker_function(self, to_parsed):
		j = 1
		#Html_file = open("output.html","w")
		for i in to_parsed:
			with TelegramClient('account'+str(j), api_id, api_hash) as client:
				try:
					html_str = """
                                                <table border=1>
                                                     <tr>
                                                         <th>Title</th>
                                                         <th>Link</th>
                                                     </tr>
                                                        <indent>
                                                     <% for i in to_parsed: %>
                                                        <tr>
                                                                 <td><%= client(functions.messages.CheckChatInviteRequest(hash=i)) %></td>
                                                                 <td><%= str(result).split("title='")[1].split("'")[0] %></td>
                                                        </tr>
                                                     </indent>
                                                </table>
                                        """
                                        with open("output.html","w") as fp:
                                                fp.write(html_str)
                                       
                                       # Html_file.write(html_str)
                                       # Html_file.close()
				except Exception as e:
					#print(e)
                        
					try:
						result = client.get_entity(i)
						title = str(result).split("title='")[1].split("'")[0]
						print("https://t.me/"+i+" "+title)
					except Exception as e:
						#print(e)
						if str(e)[0:2] != "No":
							pass
			if int(self.value_accounts) >= (j+1):
				j = j + 1
				#print("меняем акк на {0}".format(str(j)))
			else:
				j = 1
				#print("меняем акк на 1")
				
				

while True:
	App()

	




