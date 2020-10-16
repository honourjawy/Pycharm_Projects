# # encoding:utf-8
# import requests
# api = "https://sc.ftqq.com/SCU101527Ta1232e1427cdbe7d71a77c0b7d24b3c25ee44eaea7769.send"
# title = u"紧急通知"
# content = """
# #服务器又炸啦！
# ##请尽快修复服务器
# """
# data = {
#    "text":title,
#    "desp":content
# }
# req = requests.post(api,data = data)






# 学习
#
#
# #!/usr/bin/python3
# # -*- coding: utf-8 -*-
#
# import requests
# import time
# from apscheduler.schedulers.blocking import BlockingScheduler
#
# server_url = "https://sc.ftqq.com/*******************.send"
# soup_url = "http://open.iciba.com/dsapi/"
# weather_url = "restapi.amap.com/v3/weather/weatherInfo?key=****************&city=*******"
#
# scheduler = BlockingScheduler()
#
#
# def get_time():
#     """
#     获取当前时间
#     """
#     return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#
#
# def push_wx(text=None, desp=""):
#     """
#     推送消息到微信
#     """
#     params = {
#         "text": text,
#         "desp": desp
#     }
#
#     response = requests.get(server_url, params=params)
#     json_data = response.json()
#
#     if json_data['errno'] == 0:
#         print(get_time() + " 推送成功。")
#     else:
#         print("{0} 推送失败：{1} \n {2}".format(get_time(), json_data['errno'], json_data['errmsg']))
#
#
# def get_soup():
#     """
#     获取鸡汤
#     """
#     response = requests.get(soup_url)
#     json_data = response.json()
#
#     date = json_data['dateline']
#     content = json_data['content']
#     note = json_data['note']
#     picture = json_data['picture']
#     translation = json_data['translation']
#
#     return date, content, note, picture, translation
#
#
# def get_weather():
#     """
#     获取天气
#     """
#     response = requests.get(weather_url)
#     json_data = response.json()
#
#     if json_data['status'] == '1':
#         return json_data['forecasts'][0]['casts'][0]
#     else:
#         print(get_time() + " 天气获取失败：" + json_data['info'])
#         return None
#
#
# def make_soup():
#     """
#     制作鸡汤
#     """
#     soup = get_soup()
#
#     weather = get_weather()
#
#     if weather is None:
#         time.sleep(3)
#         weather = get_weather()
#
#     title = "早上好！"
#     desp = "#### {date}\n\n白天{dayweather}，夜晚{nightweather}，温度{nighttemp}℃ ~ {daytemp}℃。\n\n" \
#            "*{content}*\n\n{note}\n\n![]({picture})\n\n{translation}" \
#         .format(date=soup[0], dayweather=weather['dayweather'], nightweather=weather['nightweather'],
#                 nighttemp=weather['nighttemp'], daytemp=weather['daytemp'],
#                 content=soup[1],
#                 note=soup[2],
#                 picture=soup[3],
#                 translation=soup[4])
#
#     push_wx(title, desp)
#
# if __name__ == '__main__':
#     print(get_time() + " 开始执行任务")
#     scheduler.add_job(make_soup, 'cron', day_of_week='0-6', minute=00, second=00)
#     scheduler.start()
#
#
#


# -*- coding: utf8 -*-
# import json
#
#
# def main_handler(event, context):
# # !/usr/bin/python3
# # -*- coding: utf-8 -*-
#
#     import requests
#     import time
#     from apscheduler.schedulers.blocking import BlockingScheduler
#
#     server_url = "https://sc.ftqq.com/SCU101527Ta1232e1427cdbe7d71a77c0b7d24b3c25ee44eaea7769.send"
#     soup_url = "http://open.iciba.com/dsapi/"
#     weather_url = "restapi.amap.com/v3/weather/weatherInfo?key=8c076bafc7b112a4e141f765ae127307&city=110101"
#
#     scheduler = BlockingScheduler()
#
#     def get_time():
#         """
#         获取当前时间
#         """
#         return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#
#     def push_wx(text=None, desp=""):
#         """
#         推送消息到微信
#         """
#         params = {
#             "text": text,
#             "desp": desp
#         }
#
#         response = requests.get(server_url, params=params)
#         json_data = response.json()
#
#         if json_data['errno'] == 0:
#             print(get_time() + " 推送成功。")
#         else:
#             print("{0} 推送失败：{1} \n {2}".format(get_time(), json_data['errno'], json_data['errmsg']))
#
#     def get_soup():
#         """
#         获取鸡汤
#         """
#         response = requests.get(soup_url)
#         json_data = response.json()
#
#         date = json_data['dateline']
#         content = json_data['content']
#         note = json_data['note']
#         picture = json_data['picture']
#         translation = json_data['translation']
#
#         return date, content, note, picture, translation
#
#     def get_weather():
#         """
#         获取天气
#         """
#         response = requests.get(weather_url)
#         json_data = response.json()
#
#         if json_data['status'] == '1':
#             return json_data['forecasts'][0]['casts'][0]
#         else:
#             print(get_time() + " 天气获取失败：" + json_data['info'])
#             return None
#
#     def make_soup():
#         """
#         制作鸡汤
#         """
#         soup = get_soup()
#
#         weather = get_weather()
#
#         if weather is None:
#             time.sleep(3)
#             weather = get_weather()
#
#         title = "早上好！"
#         desp = "#### {date}\n\n白天{dayweather}，夜晚{nightweather}，温度{nighttemp}℃ ~ {daytemp}℃。\n\n" \
#                "*{content}*\n\n{note}\n\n![]({picture})\n\n{translation}" \
#             .format(date=soup[0], dayweather=weather['dayweather'], nightweather=weather['nightweather'],
#                     nighttemp=weather['nighttemp'], daytemp=weather['daytemp'],
#                     content=soup[1],
#                     note=soup[2],
#                     picture=soup[3],
#                     translation=soup[4])
#
#         push_wx(title, desp)
#
#         print(get_time() + " 开始执行任务")
#         # scheduler.add_job(make_soup, 'cron', day_of_week='0-6', minute=00, second=00)
#         scheduler.start()


# -*- coding: utf8 -*-
import requests


def main_handler(*arg):
    def get_iciba_everyday():
        icbapi = 'http://open.iciba.com/dsapi/'
        eed = requests.get(icbapi)
        bee = eed.json()  # 返回的数据
        english = eed.json()['content']
        zh_CN = eed.json()['note']
        str = '\n\n【给jawy的一句话】\n\n' + english + '\n\n' + zh_CN
        return str

    # 天气
    key = 'https://sc.ftqq.com/SCU101527Ta1232e1427cdbe7d71a77c0b7d24b3c25ee44eaea7769.send'  # 填自己的key
    cpurl = key
    api = 'http://t.weather.itboy.net/api/weather/city/'                                      # API地址，必须配合城市代码使用
    city_code = '101100101'                # 进入[url=https://where.heweather.com/index.html]https://where.heweather.com/index.html[/url]查询你的城市代码
    tqurl = restapi.amap.com/v3/weather/weatherInfo?key=8c076bafc7b112a4e141f765ae127307&city=110101
    response = requests.get(tqurl)
    d = response.json()                     # 将数据以json形式返回，这个d就是返回的json数据

    if (d['status'] == 200):  # 当返回状态码为200，输出天气状况
        print("城市：", d["cityInfo"]["parent"], d["cityInfo"]["city"])
        print("更新时间：", d["time"])
        print("日期：", d["data"]["forecast"][0]["ymd"])
        print("星期：", d["data"]["forecast"][0]["week"])
        print("天气：", d["data"]["forecast"][0]["type"])
        print("温度：", d["data"]["forecast"][0]["high"], d["data"]["forecast"][0]["low"])
        print("湿度：", d["data"]["shidu"])
        print("PM25:", d["data"]["pm25"])
        print("PM10:", d["data"]["pm10"])
        print("空气质量：", d["data"]["quality"])
        print("风力风向：", d["data"]["forecast"][0]["fx"], d["data"]["forecast"][0]["fl"])
        print("感冒指数：", d["data"]["ganmao"])
        print("温馨提示：", d["data"]["forecast"][0]["notice"], "。")

        tdwt = '\n\n城市：' + d['cityInfo']['parent'] + ' ' + d['cityInfo']['city'] + '\n\n日期：' + d["data"]["forecast"][0][
            "ymd"] + ' ' + d["data"]["forecast"][0]["week"] + '\n\n天气：' + d["data"]["forecast"][0]["type"] + '\n\n温度：' + \
               d["data"]["forecast"][0]["high"] + ' ' + d["data"]["forecast"][0]["low"] + '\n\n湿度：' + d["data"][
                   "shidu"] + '\n\n空气质量：' + d["data"]["quality"] + '\n\n风力风向：' + d["data"]["forecast"][0]["fx"] + ' ' + \
               d["data"]["forecast"][0]["fl"] + '\n\n温馨提示：' + d["data"]["forecast"][0]["notice"] + '。\n\n[更新时间：' + d[
                   "time"] + ']\n\n-----------------' + get_iciba_everyday()  # 天气提示内容，基本上该有的都做好了，如果要添加信息可以看上面的print，我感觉有用的我都弄进来了。
        text = "【今日份天气】"
        data = {'text': text, 'desp': tdwt.encode('UTF-8')}
        res = requests.post(cpurl, data=data)  # 把天气数据转换成UTF-8格式，不然要报错。
        print(res.text)
    else:
        error = '【出现错误】\n　　今日天气推送错误，请检查服务状态！'
        res = requests.post(cpurl, error.encode('utf-8'))
        print(res.text)






