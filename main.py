#!/usr/bin/python3


import requests

from requests.structures import CaseInsensitiveDict

url = "https://api.iot.yandex.net/v1.0/devices/тут id устройства"  #Заменить "тут id устройства" на ID своего датчика

headers = CaseInsensitiveDict()

headers={"Authorization": "Bearer токен"} #Заменить слово "токен" своим токеном авторизации
try:
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()  # Вызывает исключение, если ответ содержит ошибку HTTP
    resps = resp.json()

    for key, values in resps.items():
        if key == 'properties':
            for z in values:
                z = dict(z)
                for keyz, valuez in z.items():
                    if keyz == 'state':
                        nameelement = "тут указываем путь для создания файлов с данными" + valuez.get('instance')
                        print(valuez.get('value'))
                        with open(nameelement, "w+") as text_file:
                            text_file.write(str(valuez.get('value')))
except requests.exceptions.RequestException as e:
    print("Request failed:", e)
except ValueError as ve:
    print("Error decoding JSON:", ve)