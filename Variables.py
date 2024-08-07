import time
import configparser

config = configparser.ConfigParser()
config.read('DATA.ini', encoding='utf-8')


another_token = config['DEFAULT']['another_token']
promt = config['DEFAULT']['promt']
version = config['DEFAULT']['version']
time_end = int(config['DEFAULT']['time_end'])
name_OPENVPN_Linux = config['DEFAULT']['name_OPENVPN_Linux']
name_OPENVPN_Win = config['DEFAULT']['name_OPENVPN_Win']
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
type_mes = ''
already_processed_photo_text_ = False
already_processed_photo_text_2 = False
my_id = '545067517'
paused = False
command = f'nmcli connection up {name_OPENVPN_Linux}'
command2 = f'"C:\\Program Files\\OpenVPN\\bin\\openvpn-gui.exe" --command connect {name_OPENVPN_Win}.ovpn'
