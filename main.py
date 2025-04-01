import requests
from time import sleep

TOKEN = '6996163606:AAEKw639tINrZJRmoy6-kCjmVZ-UMHgV7go'
CHAT_ID = '-4207787304'


# i =1
# try:
#     MY_MESSAGE_TEXT = f'Server Live on: {i}s'
#     requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={MY_MESSAGE_TEXT}')
#     sleep(10)
# except:
#     print('Send Requests Fail')


i = 1
while True:
    try:
        MY_MESSAGE_TEXT = f'Server Live on: {i}s'
        print(MY_MESSAGE_TEXT)
        requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={MY_MESSAGE_TEXT}')
        sleep(10)
        i +=10
    except:
        print('Send Requests Fail')
