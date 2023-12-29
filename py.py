import requests
import time


token = '2ac52c402ac52c402ac52c40ad29d3edae22ac52ac52c404f485bcc3b184095b84a36bc'
another_token = 'vk1.a.IiKqzHpfPFaZVNeXr6lK6RZ-6gMnpxM-WvIFc7pzTzU3W5gP2ZxdFZgO35iZFF9-zhNSuaHBP3aDhY6NC9Ufn-VomQyToIhmRQHZeHQXSbzTe9M3WrtdvAK1qR_1aEupQuyokaa1BAnM3PRzmhFZEnylfPRRR3xKkhlcfKCN2WOqcLvLMSzo0BJrWCX_XF2yttSGKfpAtdkwWHgLvBLEnQ'
my_id = '545067517'
version = 5.199
domain = 'strongmennewschool'
a = 0
while True:
    response = requests.get(
        'https://api.vk.com/method/wall.get',
        params={
            'count': 2,
            'filter': 'owner, others',
            'access_token': token,
            'v': version,
            'domain': domain
        
        }
    )
    data = response.json()['response']['items']


    text = ''
    photo_urls = []

    for post in data:
        post_text = post.get('text', '')
        text += post_text + '\n'

        attachments = post.get('attachments', [])
        for attachment in attachments:
            if attachment['type'] == 'photo':
              
                photo_url = attachment['photo']['sizes'][-1]['url']
                photo_urls.append(photo_url)

    print(text)
    print(photo_urls)
       
        

    w = requests.get(
        'https://api.vk.com/method/status.set',
        params={
            'access_token': another_token,
            'text': text,    
            'group_id': my_id,    
            'attachment': ','.join(photo_urls),
            'v': version
        }
   
    )

    c = requests.get(
        'https://api.vk.com/method/messages.send',
        params={
            'access_token': another_token,
            'user_id': my_id,
            'random_id': 0,
            'message': text,
            'v': version
        }
    )
   
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
    print('круг пройден:', a )
    time.sleep(20)  
