# -*- coding: utf8 -*-
import requests
import datetime

def main_handler(*arg):
    def get_iciba_everyday():
        icbapi = 'http://open.iciba.com/dsapi/'
        eed = requests.get(icbapi)
        bee = eed.json()               # 返回的数据
        english = eed.json()['content']
        zh_CN = eed.json()['note']
        strr = '\n\n【给jawy的一句话】\n\n' + english + '\n\n' + zh_CN
        return strr

    key = 'https://sc.ftqq.com/SCU101527Ta1232e1427cdbe7d71a77c0b7d24b3c25ee44eaea7769.send'  # 填自己的key
    cpurl = key

    def diyText():
        today = datetime.date.today()
        nianjieshu_day = datetime.date(2020, 12, 31)  # 2020结束天数
        yanjieshu_day = datetime.date(2023, 7, 1)     # 研究生阶段结束天数
        siliuji_day = datetime.date(2020, 12, 12)       # 四六级剩余天数
        date1 = (nianjieshu_day - today).days
        date2 = (yanjieshu_day - today).days
        date3 = (siliuji_day - today).days
        # api = 'http://t.weather.itboy.net/api/weather/city/'  # API地址，必须配合城市代码使用
        # city_code = '101010100'
        # tqurl = api + city_code
        # response = requests.get(tqurl)
        # d = response.json()  # 将数据以json形式返回，这个d就是返回的json数据
        # data = str(print("日期：", d["data"]["forecast"][0]["ymd"]))
        # weather = str(print("天气：", d["data"]["forecast"][0]["type"], d["data"]["forecast"][0]["high"],
        #       d["data"]["forecast"][0]["low"]))

        content = ("> 你说:在关于未来的那个相逢里，愿都能蜕变成最精彩的模样。 \n\n"
                   "------\n"
                   "### **任务分析**：\n" + str('') + "\n\n"
                   "| 今日清单: |   " + str('要求') + "|\n"
                   "| -------- | :----------------:|\n"
                   "| 👀视力保健: |   " + str('10分钟') + "|\n"
                   "| 🆎墨墨背单词: |   " + str('1小时') + "|\n"
                   "| 👄口腔/下巴: |   " + str('5分钟') + "|\n"
                   "| 💻Python: |   " + str('2小时') + "|\n"
                   "| 🏃跑步: |   " + str('30分钟') + "|\n"  
                   "| 🎧Listening: |   " + str('15分钟') + "|\n"                                 
                   "| ❤签到: |   " + str('WPS,三国杀') + "|\n"
                           
                   "------\n"
                   "### **时间状态**：\n" + str('') + "\n\n"
                   "**四六级倒计时**:\n距四六级考试还有" + str(date3) + "天，单词背了多少？\n"
                   "\n\n"
                   "**2020倒计时**:\n距2020结束还有" + str(date1) + "天，任务完成了没有？\n"
                   "\n\n"
                   "**研究生倒计时**:\n距研究生结束结束还有" + str(date2) + "天，jawy，珍惜时间！\n"
                   

                   )
        return content

    expression = diyText() + '\n\n--------------' + get_iciba_everyday()
    text = "-----> jawy"
    data = {'text': text, 'desp': expression.encode('UTF-8')}        # 把数据转换成UTF-8格式，不然要报错。
    res = requests.post(cpurl, data=data)
    print(res.text)

api = 'http://t.weather.itboy.net/api/weather/city/'  # API地址，必须配合城市代码使用
city_code = '101010100'
tqurl = api + city_code
response = requests.get(tqurl)
d = response.json()  # 将数据以json形式返回，这个d就是返回的json数据
print("日期：", d["data"]["forecast"][0]["ymd"])
print("天气：", d["data"]["forecast"][0]["type"],d["data"]["forecast"][0]["high"], d["data"]["forecast"][0]["low"])