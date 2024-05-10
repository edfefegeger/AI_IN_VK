import requests
from Variables import another_token, promt, version, time_end, name_OPENVPN_Linux, name_OPENVPN_Win, num, num2, processed_messages, processed_messages2, a, b, count, count2, conversation, conversation2, start, minutes, ischatter, ischatter2, user_texter2, id_caught, id_caught2, Not_paused, type_mes, already_processed_photo_text_, already_processed_photo_text_2, my_id, domain, paused

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