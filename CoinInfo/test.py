# -*-coding:utf-8-*-

# 抓取币种信息

import requests,re,time
import os
import random
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

ua_list = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
        "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
]

user_agent=random.choice(ua_list)

# 获取数据函数
def get_data(url,user_agent):
	request=requests.get(url=url)
	request.encoding='uft-8'
	request.headers=user_agent
	response=request.text
	soup_pre=BeautifulSoup(response,"lxml")
	return soup_pre

# 获取币种列表
url_index='https://coinmarketcap.com/'
data_coin = get_data(url_index, user_agent)
coin_list = []
for i in data_coin.find_all(class_='currency-name-container link-secondary'):
	coin_list.append(i.get_text()) # 需要抓取href链接，然后取中间的名字

# 构造URL，可以利用list创建待查询的币种
for Coin_Name in coin_list:
	if Coin_Name=='XRP':
		Coin_Name='ripple'
	elif Coin_Name=='Bitcoin Cash':
		Coin_Name='bitcoin-cash'
	Coin_url="https://coinmarketcap.com/currencies/"+Coin_Name

	# 抓取币种信息
	data = get_data(Coin_url, user_agent)
	for i in data.find_all(class_='h2 text-semi-bold details-panel-item--price__value'):
		coin_price=i.get_text() #币价
	for i in data.find_all(class_='label label-success'):
		coin_rank=i.get_text().split(' ')[-1] #市值排名,不能抓取最后一个字符
	for i in data.find_all(class_='details-panel-item--marketcap-stats flex-container'):
		coin_MarketCap=re.search(r'data-usd="'+'\d+', str(i)).group().split('"')[-1] # 流通市值,比特币的值是科学计数法，会出现获取错误
	for i in data.find_all(class_='details-panel-item--marketcap-stats flex-container'):
		coin_Volume24h=re.search(r'data-currency-volume="" data-usd="'+'\d+', str(i)).group().split('"')[-1] # 24H交易量
	for i in data.find_all(class_='details-panel-item--marketcap-stats flex-container'):
		coin_CirculatingSupply=re.search(r'data-format-supply="" data-format-value="'+'\d+', str(i)).group().split('"')[-1] # 流通量
	print('币名:'+Coin_Name+' | ','排名：'+coin_rank+' | ','币价:'+coin_price+' | ','交易量：'+coin_Volume24h+' | ','市值:'+coin_MarketCap+' | ','流通量：'+coin_CirculatingSupply+' | ')

	time.sleep(3)



# 下一步把抓取的信息存入mysql





#<span data-format-supply="" data-format-value="101177428.249">101,177,428</span>

'''
page_count1=0
page_count2=1

while page_count2>page_count1:
	url=url_pre+str(page_count2)
	geturl1=get_data(url,user_agent)
	soup=geturl1.find_all(class_='pagelist')
	for a in soup:
		a=a.get_text(',')
		a=a.split(',')
		page_count1=int(a[-2])
	if a[-1]!='下一页':
		break

	print('正在计算总页数，已搜索到第%s页' %page_count1)
	url2=url_pre+str(page_count1)
	geturl2=get_data(url2,user_agent)
	soup1=geturl2.find_all(class_='pagelist')
	for a1 in soup1:
		a1=a1.get_text(',')
		a1=a1.split(',')
		page_count2=int(a1[-2])
	if a1[-1]!='下一页':
		break

if page_count1>page_count2:
	page_count=page_count1
else:
	page_count=page_count2
# 得用类解决上边代码重复问题


page_number_s=0
# 图片总页数，待更新自动获取总页数。
#page_count=1
print('计算完成，关键词为%s的图片总计有%s页' %(Img_Name,page_count))

print('现在开始下载...')
for p in range(page_count):
	page_number_s=page_number_s+1
	page_number=str(page_number_s)

	# 构建URL
	url3=url_pre+page_number
	# 通过Request()方法构造一个请求对象
	getimg=get_data(url3,user_agent)
	#如出现编码错误，试试这个 response.encoding=('utf-8', 'ignore')
	#.decode('utf-8', 'ignore').replace(u'\xa9', u'')
	soup3=getimg.find_all(class_='il_img')
	img_name=0
	for i in soup3:
		img_name=img_name+1
		for ii in i.find_all('a'):
			# 可以直接取属性获得href内容 https://bbs.csdn.net/topics/392161042?list=lz
			urlimg='http://www.ivsky.com'+ii['href']
			getimg2=get_data(urlimg,user_agent)
			soupimg=getimg2.find_all(id='imgis')

			for img in soupimg:
				img_url=img.get('src')
				img_name_=img.get('alt')

			# 这是MAC下的目录
			#urllib2.urlretrieve(img_url,'/Users/lhuibin/py/img/%s%s.jpg' % (page_number_s,img_name))
			# 如果文件夹不存在，则创建文件夹			
			if 'img' not in os.listdir():
				os.makedirs('img')

			# 这是WIN10HOME下的目录
			urlretrieve(img_url,'img/%s%s%s.jpg' % (img_name_,page_number_s,img_name))
			print('正在下载第%s页第%s张图片，总计%s页' %(page_number_s,img_name,page_count))
			print('存储为img/%s%s%s.jpg' % (img_name_,page_number_s,img_name))

print("已经全部下载完毕！")
'''