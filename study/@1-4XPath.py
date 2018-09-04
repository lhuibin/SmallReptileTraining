# xpath用法整理：https://blog.csdn.net/u013332124/article/details/80621638
import requests,io,sys,pandas


sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') #改变标准输出的默认编码


from lxml import etree

url = 'http://sz.xiaozhu.com/'

r = requests.get(url).text#使用requests获取数据

s = etree.HTML(r)#解析html数据

title = s.xpath('//*[@id="page_list"]/ul/li/div[2]/div/a/span/text()')#打印短租标题

price = s.xpath('//*[@id="page_list"]/ul/li/div[2]/span[1]/i/text()')#打印短租价格

latlng = s.xpath('//*[@id="page_list"]/ul/li/@latlng')#打印短租经纬度

print(list(i for i in zip(title,price,latlng)))