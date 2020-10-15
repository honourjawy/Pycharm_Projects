# import pandas as pd
# print(pd.DataFrame())

import requests
api = 'http://t.weather.itboy.net/api/weather/city/'  # API地址，必须配合城市代码使用
city_code = '101010100'
tqurl = api + city_code
response = requests.get(tqurl)
d = response.json()  # 将数据以json形式返回，这个d就是返回的json数据
print("日期：", d["data"]["forecast"][0]["ymd"])
print("天气：", d["data"]["forecast"][0]["type"],d["data"]["forecast"][0]["high"], d["data"]["forecast"][0]["low"])