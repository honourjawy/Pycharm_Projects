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

    tdwt = '哇啊家居安静安静' + ']\n\n-----------------' + get_iciba_everyday()
    text = "【致jawy】"
    data = {'text': text, 'desp': tdwt.encode('UTF-8')}    # 把数据转换成UTF-8格式，不然要报错。
    res = requests.post(cpurl, data=data)
    print(res.text)

