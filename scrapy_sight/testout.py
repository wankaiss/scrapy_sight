# -*- coding:utf-8 -*-
import re
import urllib
# text = u'中国地标建筑'.encode('utf-8')
# result = text.replace('旅游攻略（', '')

str_text = u'/search/detail?ct=503316480&isflip=1&z=undefined&tn=baiduimagedetail&ipn=d&word=%E4%B8%8A%E6%B5%B7%E4%B8%AD%E5%BF%83%E5%A4%A7%E5%8E%A6&ie=utf-8&in=0&cl=0&lm=0&st=0&cs=953421704,3740952869&os=1705981024,1455000635&adpicid=0&pn=0&rn=1&di=128192134510&ln=1973&fr=0&fm=&fmq=&ic=0&s=0&se=0&sme=0&tab=0&width=&height=&face=undefined&is=0,0&istype=2&ist=0&jit=0&bdtype=0&gsm=0&pi=0&objurl=http%3A%2F%2Fwww.archreport.com.cn%2Fuploadfile%2F2015%2F1125%2F20151125032333980.jpg&rpstart=0&rpnum=0'

result = re.search(r'.*objurl=(http.*?)&.*', str_text).groups()[0]
quote = urllib.unquote(urllib.unquote(result))

print quote
