import requests
import time



# Запрос на сервер методом POST
url = 'http://api.lbs.yandex.net/geolocation'
# Открытие файла

file = open('response.txt', 'w')
for cid in range(4000, 5000):
    time.sleep(0.01)
    payload = "json={\r\n   \"common\": {\r\n      \"version\": \"1.0\",\r\n      \"api_key\": " \
              "\"AAWW1l0BAAAA-ySjGQIAJGp8BARUCie1PUbaznYu58C8xzcAAAAAAAAAAABF0LkL4ONOCjhC_WbHUrN__bCa6w==\"\r\n   }," \
              "\r\n   \"gsm_cells\": [\r\n       {\r\n          \"countrycode\": 250,\r\n          \"operatorid\": 99," \
              "\r\n          \"cellid\": " + str(cid) + ",\r\n          \"lac\": 14752,\r\n   \"signal_strength\": -80," \
              "\r\n          \"age\": 1000\r\n       }\r\n   ],\r\n   \"wifi_networks\": [\r\n       {\r\n          " \
              "\"mac\": \"2CD02D814C80\",\r\n          \"signal_strength\": -68,\r\n          \"age\": 500,\r\n       }," \
              "\r\n       {\r\n          \"mac\": \"E4AA5DE28CD0\",\r\n          \"signal_strength\": -60,\r\n          " \
              "\"age\": 500,\r\n       }\r\n   ],\r\n   \"ip\": {\r\n     \"address_v4\": \"95.108.173.231\"\r\n   }\r\n} "
    headers = {'content-type': 'application/json'}
    response = requests.post(url=url, data=payload, headers=headers)
    response = response.text
    response = str(response)
    file.write(response)
    print(response)

# response = requests.post('https://httpbin.org/post', data={'key':'value'})

file.close()



