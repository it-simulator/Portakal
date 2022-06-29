#команды в cmd для установки модуля httpx: 
#C:\Users\Administrator>cd C:\Users\Administrator\AppData\Local\Programs\Python\Python310\Scripts
#C:\Users\Administrator\AppData\Local\Programs\Python\Python310\Scripts>pip install httpx

#еще 1 способ получения contents (через urllib)
#import urllib.request

import httpx
import time
import re

update_id = None
i=1
while True:
    
    contents = httpx.get('https://api.telegram.org/bot5424003728:AAGxoRyIhNvKJpoMVm_1cRKbtVyve6BgHhI/getUpdates')
    #contents = urllib.request.urlopen('https://api.telegram.org/bot5424003728:AAGxoRyIhNvKJpoMVm_1cRKbtVyve6BgHhI/getUpdates').read()

    updates = contents.json()
    message = updates['result']
    new_update_id = message[-1]['update_id']
    print(message.text)
    if new_update_id != update_id:
        update_id = new_update_id
        message_fix = message[-1]['message']
        chat_id=message_fix['chat']['id']
        if i==1:
           httpx.get('https://api.telegram.org/bot5424003728:AAGxoRyIhNvKJpoMVm_1cRKbtVyve6BgHhI/sendMessage?chat_id=612970508&text=Доброго времени суток. Для регистрации укажите адрес эл.почты')
           i=2
        else:
           email = message_fix['text']
           regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
           if re.fullmatch(regex, email):
               httpx.get('https://api.telegram.org/bot5424003728:AAGxoRyIhNvKJpoMVm_1cRKbtVyve6BgHhI/sendMessage?chat_id=612970508&text=Адрес эл.почты зарегистрирован') 
           else:
               httpx.get('https://api.telegram.org/bot5424003728:AAGxoRyIhNvKJpoMVm_1cRKbtVyve6BgHhI/sendMessage?chat_id=612970508&text=Адрес эл.почты не соответствует формату') 
time.sleep(1)
