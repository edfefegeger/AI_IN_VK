from operator import floordiv
import keyboard
import requests
import time
import openai
import random
from art import tprint
import os
import subprocess
from print import log_and_print

tprint("Ai_in_Vk")
tprint("WELCOME")

with open("DATA.ini", 'r', encoding='utf-8') as r:
    another_token = r.readline().strip()
    openai.api_key = r.readline().strip()
    promt = r.readline().strip()
    version = r.readline().strip()
    time_end = int(r.readline().strip())
    name_OPENVPN_Linux = r.readline().strip()
    name_OPENVPN_Win = r.readline().strip()

command = f'nmcli connection up {name_OPENVPN_Linux}'
command2 = f'"C:\\Program Files\\OpenVPN\\bin\\openvpn-gui.exe" --command connect {name_OPENVPN_Win}.ovpn'



if os.name == "posix":
    try:
        os.system(command)
        log_and_print("VPN успешно подключен на Linux/Unix.")
    except:
        log_and_print("Ошибка при подключении к VPN")

if os.name == "nt":
    try:
        subprocess.run(command2, check=True, shell=True)
        log_and_print("VPN успешно подключен на Windows.")
    except subprocess.CalledProcessError:
        log_and_print("Ошибка при подключении к VPN")
    
my_id = '545067517'
domain = 'strongmennewschool'

num = True
num2 = True
processed_messages = set() 
processed_messages2 = set() 
a = 0
b = 1
count = 0
count2 = 0
conversation = [{"role": "system", "content":  promt}] 
conversation2 = [{"role": "system", "content":  promt}] 
start = time.time()
minutes = 0
ischatter = None
ischatter2 = None
user_texter2 = None
id_caught = None
id_caught2 = None
Not_paused = False
def toggle_pause():
    global paused
    paused = not paused
    global Not_paused
    Not_paused = False
    log_and_print("Нажато '-'")
def toggle_pause2():
    global paused
    paused = False
    global Not_paused
    Not_paused = True
    log_and_print("Нажато '+'")
paused = False

keyboard.add_hotkey('-', toggle_pause)
keyboard.add_hotkey('+', toggle_pause2)

get_long_poll = requests.get(
         'https://api.vk.com/method/messages.getLongPollServer',
         params={
             'access_token': another_token,
             'v': version
         }
    )

response_json_ts = get_long_poll.json()
ts = response_json_ts.get('response', {}).get('ts', [])
log_and_print("ts:", ts)

try:
    while not paused or paused:
        long_poll = requests.get(
          'https://api.vk.com/method/messages.getLongPollHistory',
          params={
              'access_token': another_token,
              'ts': ts,
              'v': version
          }
      )
        long_poll_history = long_poll.json()
        message_count = long_poll_history.get('response', {}).get('messages', '')
        message_conv = long_poll_history.get('response', {}).get('conversations', [])
        message_count2 = message_count.get('count', '')
        log_and_print("Количество сообщений:", message_count2)
  
        if message_count2 != 0 :
            if id_caught != message_conv[0].get('peer', {}).get('id', ''):
              user_texter = message_conv[0].get('peer', {}).get('id', '')
              user_typer = message_conv[0].get('peer', {}).get('type', '')     
              
              id_caught = user_texter
              zhitenev_id = id_caught
              chatter = id_caught
              ischatter = True
  
              if len(message_conv) >= 1.5:
                  user_texter2 = True
  
        if len(message_conv) > 1:
            if id_caught2 != message_conv[1].get('peer', {}).get('id', ''):
              user_texter2 = message_conv[1].get('peer', {}).get('id', '')
              user_typer2 = message_conv[1].get('peer', {}).get('type', '')           
              
              id_caught2 = user_texter2
              zhitenev_id2 = id_caught2
              chatter2 = id_caught2
              ischatter2 = True
            
        if ischatter == True and user_typer == 'user': 
          if num == True:  
              log_and_print("Первый найден",user_texter, user_typer)    
              num = False
  
          messages = requests.get(
              'https://api.vk.com/method/messages.getHistory',
              params={
                  'access_token': another_token,
                  'count': 25,
                  'user_id': zhitenev_id,
                  'rev': 0,
                  'v': version
              }
          )
          response_json = messages.json()
          if 'error' in response_json:
              log_and_print(f"Error from VK API: {response_json['error']['error_msg']}")
          else:
              items = response_json.get('response', {}).get('items', [])
              for item in items:
                  message_id = item.get('id', '')
                  if message_id in processed_messages:
                      log_and_print("Сообщение уже обработано")
                      break
                  processed_messages.add(message_id) 
                  text = item.get('text', '')  
                  if count == 0:
                      conversation.append({"role": "user", "content": text})
                      count += 1
                  message_from = item.get('from_id', '')   
                  type_message = item.get('type', '') 
                  attachments = item.get('attachments', []) 
                  for attachment in attachments:
                      type_mes = attachment.get('type', '')
                      log_and_print("Тип Вложения:", type_mes)
                      if message_from == chatter and type_mes == 'wall':
                          log_and_print("Сообщение от жертвы", message_from)
                          finally_message_404 = requests.get(
                              
                                  'https://api.vk.com/method/messages.send',
                                  params={
                                  'access_token': another_token,
                                  'user_id': zhitenev_id,
                                  'random_id': 0,
                                  'attachment': "photo545067517_457254536",
                                  'message': "Хуета ебаная",
                                  'v': version,
                                  'reply_to': message_id
                                  }
                                      )
                          break  
                      if message_from == chatter and type_mes == 'story':
                          log_and_print("Сообщение от жертвы", message_from)
                          finally_message_404 = requests.get(
                                  'https://api.vk.com/method/messages.send',
                                  params={
                                  'access_token': another_token,
                                  'user_id': zhitenev_id,
                                  'random_id': 0,
                                  'attachment': "photo545067517_457254537",
                                  'v': version,
                                  'reply_to': message_id
                                  }
                                      )
                      if message_from == chatter and type_mes == 'sticker':
                          log_and_print("Сообщение от жертвы", message_from)
                          finally_message_404 = requests.get(
                                  'https://api.vk.com/method/messages.send',
                                  params={
                                  'access_token': another_token,
                                  'user_id': zhitenev_id,
                                  'random_id': 0,
                                  'message': "Не прогрузился, напиши текстом",
                                  'attachment': "doc545067517_623985008",
                                  'v': version,
                                  'reply_to': message_id
                                  }
                                      )    
                          break
                        
                      if message_from == chatter and type_mes == 'audio_message' and text != "" :
                          transcript_message = attachment.get('audio_message', {}).get('transcript', '')
                          log_and_print("Сообщение от жертвы", message_from)
                          log_and_print(transcript_message)
                          try:
                              conversation.append({"role": "user", "content": transcript_message})
                              completion_audio = openai.ChatCompletion.create(
                              model="gpt-3.5-turbo-0613",
                              messages=conversation + [{"role": "user", "content": transcript_message}]
                              )
                              ready_audio_message = completion_audio.choices[0].message.content
                              log_and_print("Ответ GPT:", completion_audio.choices[0].message.content)
                              finally_audio_message = requests.get(
                              'https://api.vk.com/method/messages.send',
                              params={
                              'access_token': another_token,
                              'user_id': zhitenev_id,
                              'random_id': 0,
                              'message':ready_audio_message, 
                              'reply_to': message_id,
                              'v': version
                              }
                              )
                          except openai.error.APIError as e:
                              log_and_print("Ошибка от  OpeanAI, Включите VPN. Сообщение пропущено(")    
                              break
                      break
                  if message_from == chatter and text != "" :              
                      log_and_print("Сообщение от жертвы", message_from)
                      log_and_print(text)
                      try:
                          conversation.append({"role": "user", "content": text })
                          completion = openai.ChatCompletion.create(
                              model="gpt-3.5-turbo-0613",
                              messages=conversation + [{"role": "user", "content": text}]
                              )
                          ready_message = completion.choices[0].message.content
                          log_and_print("Ответ GPT:", completion.choices[0].message.content)
                          finally_message = requests.get(
                          'https://api.vk.com/method/messages.send',
                          params={
                          'access_token': another_token,
                          'user_id': zhitenev_id,
                          'random_id': 0,
                          'message':ready_message,
                          'v': version,
                          'reply_to': message_id
                          }
                              )
                      except openai.error.APIError as e:
                          log_and_print("Ошибка от  OpeanAI, Включите VPN. Сообщение пропущено(")
                          break
                      break
        if ischatter2 == True and user_typer2 == 'user':
            if num2 == True:  
               log_and_print("Второй найден",user_texter, user_typer)    
               num2 = False
            messages = requests.get(
                'https://api.vk.com/method/messages.getHistory',
                params={
                    'access_token': another_token,
                    'count': 25,
                    'user_id': zhitenev_id2,
                    'rev': 0,
                    'v': version
                }
            )
            response_json = messages.json()
            if 'error' in response_json:
                log_and_print(f"Error from VK API: {response_json['error']['error_msg']}")
            else:
                items = response_json.get('response', {}).get('items', [])
                for item in items:
                    message_id = item.get('id', '')
                    if message_id in processed_messages2:
                        log_and_print("Сообщение второй жертвы уже обработано")
                        break
                    processed_messages2.add(message_id) 
                    if count2 == 0:
                        conversation2.append({"role": "user", "content": text})
                        count2 += 1
                    text = item.get('text', '')  
                    message_from = item.get('from_id', '')   
                    type_message = item.get('type', '') 
                    attachments = item.get('attachments', []) 
                    for attachment in attachments:
                        type_mes = attachment.get('type', '')
                        log_and_print("Attachment Type:", type_mes)
                        if message_from == chatter and type_mes == 'wall':
                            log_and_print("Сообщение от второй жертвы", message_from)
                            finally_message_404 = requests.get(
                                    'https://api.vk.com/method/messages.send',
                                    params={
                                    'access_token': another_token,
                                    'user_id': zhitenev_id2,
                                    'random_id': 0,
                                    'attachment': "photo545067517_457254536",
                                    'message': "Хуета ебаная",
                                    'v': version,
                                    'reply_to': message_id
                                    }
                                        )
                            break  
                        if message_from == chatter and type_mes == 'story':
                            log_and_print("Сообщение от второй жертвы", message_from)
                            finally_message_404 = requests.get(
                                    'https://api.vk.com/method/messages.send',
                                    params={
                                    'access_token': another_token,
                                    'user_id': zhitenev_id2,
                                    'random_id': 0,
                                    'attachment': "photo545067517_457254537",
                                    'v': version,
                                    'reply_to': message_id
                                    }
                                        )
                            break
                        
                        if message_from == chatter and type_mes == 'audio_message':
                            transcript_message = attachment.get('audio_message', {}).get('transcript', '')
                            log_and_print("Сообщение от второй жертвы", message_from)
                            log_and_print(transcript_message)
  
                            conversation2.append({"role": "user", "content": transcript_message})
                            try:
                              completion_audio = openai.ChatCompletion.create(
                              model="gpt-3.5-turbo-0613",
                              messages=conversation2 + [{"role": "user", "content": transcript_message}]
                              )
                              ready_audio_message = completion_audio.choices[0].message.content
                              log_and_print("Ответ GPT:", completion_audio.choices[0].message.content)
                              finally_audio_message = requests.get(
                              'https://api.vk.com/method/messages.send',
                              params={
                              'access_token': another_token,
                              'user_id': zhitenev_id2,
                              'random_id': 0,
                              'message':ready_audio_message, 
                              'reply_to': message_id,
                              'v': version
                              }
                              )
                            except openai.error.APIError as e:
                              log_and_print("Ошибка от  OpeanAI, Включите VPN. Сообщение пропущено(")
                              break
  
                            break 
                        if message_from == chatter and type_mes == 'sticker':
                              log_and_print("Сообщение от второй жертвы", message_from)
                              finally_message_4041 = requests.get(
                                      'https://api.vk.com/method/messages.send',
                                      params={
                                  'access_token': another_token,
                                  'user_id': zhitenev_id2,
                                  'random_id': 0,
                                  'message': "Не прогрузился, напиши текстом",
                                  'attachment': "doc545067517_623985008",
                                  'v': version,
                                  'reply_to': message_id
                                  }
                                      )      
                        break
                    if message_from == chatter2 and text != "" :
                        log_and_print("Сообщение от второй жертвы", message_from)
                        log_and_print(text)
                        conversation2.append({"role": "user", "content": text })
                        try:
                          completion = openai.ChatCompletion.create(
                              model="gpt-3.5-turbo-0613",
                              messages=conversation2 + [{"role": "user", "content": text}]
                              )
                          ready_message = completion.choices[0].message.content
                          log_and_print("Ответ GPT:", completion.choices[0].message.content)
                          finally_message = requests.get(
                          'https://api.vk.com/method/messages.send',
                          params={
                          'access_token': another_token,
                          'user_id': zhitenev_id2,
                          'random_id': 0,
                          'message':ready_message,
                          'v': version,
                          'reply_to': message_id
                          }
                              )
                        except openai.error.APIError as e:
                          log_and_print("Ошибка от  OpeanAI, Включите VPN. Сообщение пропущено(")  
                          break  
                        break
        a = a + 1
        finish = time.time()
        seconds = int(finish - start)
        
        minutes = seconds // 60  # Получаем количество минут
        hours = minutes // 60  # Получаем количество часов
        minutes %= 60  # Оставляем только остаток минут
        
        log_and_print('Прошло: {} часов и {} минут'.format(hours, minutes))

  
        time_value = random.randint(12, time_end)
        log_and_print('Круг пройден: {}'.format(a))
  
        if paused == True:
            log_and_print("Пауза")
            while Not_paused == False:
                time.sleep(10)                
                with open("DATA.ini", 'r', encoding='utf-8') as r:
                    another_token = r.readline().strip()
                    openai.api_key = r.readline().strip()
                    promt = r.readline().strip()
                    version = r.readline().strip()
                    time_end = int(r.readline().strip())
                    name_OPENVPN_Linux = r.readline().strip()
                    name_OPENVPN_Win = r.readline().strip()

            print("Снятие с паузы")
    
        time.sleep(time_value)  

finally:
    log_and_print("Завершение работы")
    log_and_print("Всего сообщений: {}".format(a))
    if os.name == "posix":
        os.system('nmcli connection down vpnbook-ca149-tcp80')
        log_and_print("VPN успешно отключен на Linux/Unix.")
    elif os.name == "nt":
        subprocess.run(f'"C:\\Program Files\\OpenVPN\\bin\\openvpn-gui.exe" --command disconnect {name_OPENVPN_Win}.ovpn', check=True, shell=True)
        log_and_print("VPN успешно отключен на Windows.")