# -*-coding:utf-8-*-

# 天堂图片网爬取高质量图片


import requests
import os
import random
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

'''
# user_agent是爬虫与反爬虫斗争的第一步
ua_headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
}'''
# 用于模拟http头的User-agent
ua_list = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
        "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
]

user_agent=random.choice(ua_list)

Img_Name='小黄人'
url_pre="http://www.ivsky.com/search.php?q="+Img_Name+"&PageNo="
# 构造图片页数
# 利用抛出错误的代码，判断结果小于2也的情况


def get_data(url,user_agent):
	request=requests.get(url=url)
	request.encoding='uft-8'
	request.headers=user_agent
	response=request.text
	soup_pre=BeautifulSoup(response,"lxml")
	return soup_pre


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
