import requests
import time
import openai
import random
from art import tprint
tprint("Ai_in_Vk")
tprint("WELCOME")


with open('DATA') as r:
    another_token = r.readline().strip()
    openai.api_key = r.readline().strip()
    id_caught = int(r.readline().strip())
    id_caught2 = int(r.readline().strip())
    promt = r.readline().strip()
    version = r.readline().strip()
    time_end = int(r.readline().strip())

zhitenev_id = id_caught
chatter = id_caught
zhitenev_id2 = id_caught2
chatter2 = id_caught2
my_id = '545067517'
domain = 'strongmennewschool'
def log_and_print(*messages):
    formatted_message = ' '.join(map(str, messages))
    print(formatted_message)
    with open('LOGS', 'a') as f:
        f.write(formatted_message + '\n')

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
while True:
      user_input = input("Введите 'q' для остановки приложения")

      if user_input.lower() == 'q':
        log_and_print("Программа остановлена по запросу пользователя.")
        
        resume_input = input("Введите 's' для возобновления: ")
        if resume_input.lower() == 's':
            log_and_print("Программа возобновлена.")
            continue
        
        
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
                      break
                  
                  if message_from == chatter and type_mes == 'audio_message' and text != "" :
                      transcript_message = attachment.get('audio_message', {}).get('transcript', '')
                      log_and_print("Сообщение от жертвы", message_from)
                      log_and_print(transcript_message)
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
                  break
              if message_from == chatter and text != "" :              
                  log_and_print("Сообщение от жертвы", message_from)
                  log_and_print(text)
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
                  break
      if id_caught2 != 0:
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
                          break
                      
                      if message_from == chatter and type_mes == 'audio_message':
                          transcript_message = attachment.get('audio_message', {}).get('transcript', '')
                          log_and_print("Сообщение от жертвы", message_from)
                          log_and_print(transcript_message)
                          conversation2.append({"role": "user", "content": transcript_message})
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
                      break
                  if message_from == chatter2 and text != "" :
                      log_and_print("Сообщение от второй жертвы", message_from)
                      log_and_print(text)
                      conversation2.append({"role": "user", "content": text })
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
                      break
      a = a + 1
      finish = time.time()
      seconds = int(finish - start)
      if seconds >= 60:
          minutes += 1
          seconds -= 60
          start = time.time() 
      log_and_print('Прошло: {} минут и {} секунд'.format(minutes, seconds))

      time_value = random.randint(12, time_end)
      log_and_print('Круг пройден: {}'.format(a))


      time.sleep(time_value)  