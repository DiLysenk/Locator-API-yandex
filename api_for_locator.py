import requests

url = "http://api.lbs.yandex.net/geolocation"

payload = "json={\r\n   \"common\": {\r\n      \"version\": \"1.0\",\r\n      \"api_key\": " \
          "\"AAWW1l0BAAAA-ySjGQIAJGp8BARUCie1PUbaznYu58C8xzcAAAAAAAAAAABF0LkL4ONOCjhC_WbHUrN__bCa6w==\"\r\n   }," \
          "\r\n   \"gsm_cells\": [\r\n       {\r\n          \"countrycode\": 250,\r\n          \"operatorid\": 2," \
          "\r\n          \"cellid\": 197403650,\r\n          \"lac\": 9900,\r\n          \"signal_strength\": -80," \
          "\r\n          \"age\": 1000\r\n       }\r\n   ],\r\n   \"wifi_networks\": [\r\n       {\r\n          " \
          "\"mac\": \"2CD02D814C80\",\r\n          \"signal_strength\": -68,\r\n          \"age\": 500,\r\n       }," \
          "\r\n       {\r\n          \"mac\": \"E4AA5DE28CD0\",\r\n          \"signal_strength\": -60,\r\n          " \
          "\"age\": 500,\r\n       }\r\n   ],\r\n   \"ip\": {\r\n     \"address_v4\": \"95.108.173.231\"\r\n   }\r\n} "
headers = {'Content-Type': "application/json"}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
print()