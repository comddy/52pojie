import requests,datetime,os
from lxml import etree

today = str(datetime.date.today())

url = "https://www.52pojie.cn/forum.php?mod=guide&view=hot"
ua = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
path = "C:\\Users\\用户名\\Desktop\\52pojie.txt"
res = requests.get(url,headers=ua)
res.encoding = 'gbk'
html = etree.HTML(res.text)
urls = html.xpath("//*/tr/th/a/@href")
title = html.xpath("//*/tr/th/a/text()")
sources = ""
sources += "*************************"+today+"*************************\n" 
for _ in range(50):
	x = str(_+1)+"> "+title[_]+"  >>>  "+"https://www.52pojie.cn/"+urls[_]+"\n"
	print(x)
	sources += x
sources += "\n"
with open(path,"a+") as fp:
	fp.write(sources)
