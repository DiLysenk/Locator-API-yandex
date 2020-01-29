import requests
import time



# url - адрес запроса
url = 'http://api.lbs.yandex.net/geolocation'


# ответ если базовой станции не существует
response_BS0 = "{
   "position":
      {
         "latitude":55.75321578979492,
         "longitude":37.62250518798828,
         "altitude":0.0,
         "precision":100000.0,
         "altitude_precision":30.0,
         "type":"ip"
      }
}"

# ключ от yandex локатора
def key_yandex():
    global key
    key = "AAWW1l0BAAAA-ySjGQIAJGp8BARUCie1PUbaznYu58C8xzcAAAAAAAAAAABF0LkL4ONOCjhC_WbHUrN__bCa6w=="

# создаем список для ответок
response_list = []


# Открытие файла
key_yandex()
file = open('response.txt', 'w')
for cid in range(4000, 4002):
    time.sleep(0.01)
    payload = "json={\r\n   \"common\": {\r\n      \"version\": \"1.0\",\r\n      \"api_key\": " \
              "\"" + key + "\"\r\n   }," \
              "\r\n   \"gsm_cells\": [\r\n       {\r\n          \"countrycode\": 250,\r\n          \"operatorid\": 99," \
              "\r\n          \"cellid\": " + str(cid) + ",\r\n          \"lac\": 14752,\r\n   \"signal_strength\": -80," \
              "\r\n   \"age\": 1000\r\n    }\r\n   ],\r\n   \"wifi_networks\": [\r\n       {\r\n          " \
              "\"mac\": \"2CD02D814C80\",\r\n          \"signal_strength\": -68,\r\n          \"age\": 500,\r\n       }," \
              "\r\n       {\r\n          \"mac\": \"E4AA5DE28CD0\",\r\n          \"signal_strength\": -60,\r\n          " \
              "\"age\": 500,\r\n       }\r\n   ],\r\n   \"ip\": {\r\n     \"address_v4\": \"95.108.173.231\"\r\n   }\r\n} "
    headers = {'content-type': 'application/json'}
    response = requests.post(url=url, data=payload, headers=headers)



    # преобразовани response в текст
    response_txt = response.text

    # добавляем ответ в
    response_list.append(response_txt)
    response_set = set(response_list)

    file.write(response_txt)


print(response_set)
file.close()
# response = requests.post('https://httpbin.org/post', data={'key':'value'})
"""" ответ на несуществующую базовую станцию """



