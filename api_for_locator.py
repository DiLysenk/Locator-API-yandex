import requests
import time
import datetime
from yandex_key import YKey

# url - адрес запроса
url = 'http://api.lbs.yandex.net/geolocation'

# ответ если базовой станции не существует


# создаем список для ответок
response_list = []
cid_list = []
# код оператора
mnc = 2
# код локации
lac = 7843

# Открытие файла
file = open('response.txt', 'w')
file_cid = open('cid' + str(datetime.date.today()) + '.txt', 'w')
for cid in range(0, 5):                       # 4131, 4132, 4133
    time.sleep(0.001)
    payload = "json={\n   \"common\": {\n      \"version\": \"1.0\",\n      \"api_key\": " \
              "\"" + YKey.key + "\"\r\n   }," \
                           "\r\n   \"gsm_cells\": [\r\n       {\r\n          \"countrycode\": 250,\r\n          " \
                           "\"operatorid\": " + str(mnc) + "," \
                           "\r\n          \"cellid\": " + str(
        cid) + ",\r\n          \"lac\": " + str(lac) + ",\r\n   \"signal_strength\": -80," \
               "\r\n   \"age\": 1000\r\n    }\r\n   ],\r\n   \"wifi_networks\": [\r\n       {\r\n          " \
               "\"mac\": \"2CD02D814C80\",\r\n          \"signal_strength\": -68,\r\n          \"age\": 500," \
               "\r\n       }," \
               "\r\n       {\r\n          \"mac\": \"E4AA5DE28CD0\",\r\n          \"signal_strength\": -60,\r\n       " \
               "   " \
               "\"age\": 500,\r\n       }\r\n   ],\r\n   \"ip\": {\r\n     \"address_v4\": \"95.108.173.231\"\r\n   " \
               "}\r\n} "
    headers = {'content-type': 'application/json'}
    response = requests.post(url=url, data=payload, headers=headers)  # ответ от сервера  сервера в формате


    if list(response.text,) != ['{', '\n', ' ', ' ', ' ', '"', 'p', 'o', 's', 'i', 't', 'i', 'o', 'n', '"', ':', '\n',
                               ' ', ' ', ' ', ' ', ' ', ' ', '{', '\n', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                               '"', 'l', 'a', 't', 'i', 't', 'u', 'd', 'e', '"', ':', '5', '5', '.', '7', '5', '3', '2',
                               '1', '5', '7', '8', '9', '7', '9', '4', '9', '2', ',', '\n', ' ', ' ', ' ', ' ', ' ',
                               ' ', ' ', ' ', ' ', '"', 'l', 'o', 'n', 'g', 'i', 't', 'u', 'd', 'e', '"', ':', '3', '7',
                               '.', '6', '2', '2', '5', '0', '5', '1', '8', '7', '9', '8', '8', '2', '8', ',', '\n',
                               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '"', 'a', 'l', 't', 'i', 't', 'u', 'd', 'e',
                               '"', ':', '0', '.', '0', ',', '\n', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '"',
                               'p', 'r', 'e', 'c', 'i', 's', 'i', 'o', 'n', '"', ':', '1', '0', '0', '0', '0', '0', '.',
                               '0', ',', '\n', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '"', 'a', 'l', 't', 'i',
                               't', 'u', 'd', 'e', '_', 'p', 'r', 'e', 'c', 'i', 's', 'i', 'o', 'n', '"', ':', '3', '0',
                               '.', '0', ',', '\n', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '"', 't', 'y', 'p',
                               'e', '"', ':', '"', 'i', 'p', '"', '\n', ' ', ' ', ' ', ' ', ' ', ' ', '}', '\n', '}']:
        response_list.append(response.text)
        cid_list.append(cid)
        print(mnc, lac, cid)




response_set = set(response_list)  # преобразование списка response list в множество для создания уникальных
# значений ответов response


file.write(str(response_set)) # запись множества в файл
file_cid.write(str(cid_list))
file.close()

