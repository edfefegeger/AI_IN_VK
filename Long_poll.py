import requests
from Variables import another_token, version

def Get_Long_Poll(ts):
    if ts == None:
        Result = requests.get(
                 'https://api.vk.com/method/messages.getLongPollServer',
                 params={
                     'access_token': another_token,
                     'v': version
            }
        )

    else:
        Result = requests.get(
              'https://api.vk.com/method/messages.getLongPollHistory',
              params={
                  'access_token': another_token,
                  'ts': ts,
                  'v': version
              }
          )
    return Result