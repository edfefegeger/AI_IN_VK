import requests
import time
import openai
import random

token = '2ac52c402ac52c402ac52c40ad29d3edae22ac52ac52c404f485bcc3b184095b84a36bc'
another_token = 'vk1.a.3BiiZapxozlBzfZ5yqDehmpybegWGIa6aJOHX5lPSDSfcYDk2xh7QmQO_HOoTlhhhqLr9lzzFsaFT04OLPqcHazf-YCaY4FhzlLciy8pA0_6jvXcoP6Mf7uWGfoYFRbY5Kfg3d-waWIl6M7Ma6MCVqMPrsDzYUaGaRbvizd2-STx9mMLMpSUsGyF-U7sYuiPUjJz4Wh1ImDF9ar5rcPYDQ'
openai.api_key = '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'
promt = "Hi"

zhitenev_id = "386449723"
chatter = 386449723

my_id = '545067517'
version = 5.199
domain = 'strongmennewschool'

processed_messages = set() 

a = 0
while True:
    messages = requests.get(
        'https://api.vk.com/method/messages.getHistory',
        params={
            'access_token': another_token,
            'count': 15,
            'user_id': zhitenev_id,
            'rev': 0,
            'v': version
        }
    )
    
    response_json = messages.json()

    if 'error' in response_json:
        print(f"Error from VK API: {response_json['error']['error_msg']}")
    else:
        items = response_json.get('response', {}).get('items', [])
        

        for item in items:
            message_id = item.get('id', '')
            
            if message_id in processed_messages:
                print("Сообщение уже обработано")
                break
            processed_messages.add(message_id) 


            text = item.get('text', '')  
            message_from = item.get('from_id', '')   
            type_message = item.get('type', '') 
            attachments = item.get('attachments', []) 

            for attachment in attachments:
                type_mes = attachment.get('type', '')
                print("Attachment Type:", type_mes)

                # if type_mes == 'wall':
                #     finally_message_404 = requests.get(
                #             'https://api.vk.com/method/messages.send',
                #             params={
                #             'access_token': another_token,
                #             'user_id': zhitenev_id,
                #             'random_id': 0,
                #             'attachment': "photo""754281419""754281419",
                #             'v': version,
                #             'reply_to': message_id
                #             }
                #                 )
                #     break  

                if type_mes == 'audio_message':
                    transcript_message = attachment.get('audio_message', {}).get('transcript', '')
                    print(transcript_message)
                    completion_audio = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo-0613",
                    messages=[
                    {"role": "system", "content": "Сыграй роль аегриссивного мужика с улиц живущего по понятиям тупого и текст пиши сообщения короче"},
                    {"role": "user", "content": transcript_message},
                    ]
                    )
                    ready_audio_message = completion_audio.choices[0].message.content
                    print(completion_audio.choices[0].message.content)

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

                
                print("Сообщение от жертвы", message_from)
                print(text)
            
                completion = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo-0613",
                    messages=[
                    {"role": "system", "content": "Сыграй роль аегриссивного мужика с улиц живущего по понятиям тупого и текст пиши сообщения короче"},
                    {"role": "user", "content": text},
                    ]
                    )
                ready_message = completion.choices[0].message.content
                print(completion.choices[0].message.content)
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





               

    # response = requests.get(
    #     'https://api.vk.com/method/wall.get',
    #     params={
    #         'count': 1,
    #         'filter': 'owner, others',
    #         'access_token': token,You're an interesting conversationalist
    #     }
    # )
    # data = response.json()['response']['items']


    # text = ''
    # photo_urls = []

    # for post in data:
    #     post_text = post.get('text', '')
    #     text += post_text + '\n'

    #     attachments = post.get('attachments', [])
    #     for attachment in attachments:
    #         if attachment['type'] == 'photo':
              
    #             photo_url = attachment['photo']['sizes'][-1]['url']
    #             photo_urls.append(photo_url)

    # print(text)
       
        

    # w = requests.get(
    #     'https://api.vk.com/method/status.set',
    #     params={
    #         'access_token': another_token,
    #         'text': text,    
    #         'group_id': my_id,    
    #         'v': version
    #     }
   
    # )

    # c = requests.get(
    #     'https://api.vk.com/method/messages.send',
    #     params={
    #         'access_token': another_token,
    #         'user_id': my_id,
    #         'random_id': 0,
    #         'message': text,
    #         'attachment': ','.join(photo_urls),
    #         'v': version
    #     }
    # )
   
    # b = requests.get(
    #     'https://api.vk.com/method/wall.post',
    #     params={
    #         'access_token': another_token,
    #         'owner_id': my_id,
    #         'message': text,                  
    #         'v': version
    #     }
     
    # )
    a = a + 1
    time_value = random.randint(5, 160)
    print('Круг пройден:', a )
    time.sleep(time_value)  
