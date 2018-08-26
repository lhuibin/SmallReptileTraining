# -*-coding:utf-8-*-

# 抓取币种信息

import requests,re,time
import os
import random
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import pymysql

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
coin_list = ['bitcoin', 'bitcoin-cash', 'decred', 'nano', 'litecoin', 'bitcoin-gold', 'bitcoin-diamond', 'dogecoin', 'dash', 'monero', 'zcash', 'verge', 'particl', 'zcoin', 'ethereum', 'eos', 'cardano', 'tezos', 'bytom', 'zilliqa', 'storiqa', 'syscoin', 'cybermiles', 'neo', 'icon', 'vite', 'loopring', 'loopring-neo', 'algorand', 'ontology', 'arcblock', 'wanchain', 'pallet', '0x', 'cybereits', 'loom-network', 'bluzelle', 'fabcoin', 'cortex', 'hitchain', 'sonm', 'poet', 'decentraland', 'scryinfo', 'credits', 'jibrel-network', 'investdigital', 'baic', '0xcert', 'dock', 'libra-credit', 'smartmesh', 'rightmesh', 'blockmesh','funfair']

#coin_list = ['bitcoin', 'bitcoin-cash', 'decred']
# 自动获取币种列表
'''
url_index='https://coinmarketcap.com/'
data_coin = get_data(url_index, user_agent)
for i in data_coin.find_all(class_='currency-name-container link-secondary'):
	coin_list.append(i.get_text()) # 需要抓取href链接，然后取中间的名字
'''

# 打开数据库连接
db = pymysql.connect("localhost","root","lhuibin","mycoin" )
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
count1, count2=0,0

# 构造URL，可以利用list创建待查询的币种
for Coin_Name in coin_list:
	Coin_url="https://coinmarketcap.com/currencies/"+Coin_Name

	# SQL 查询总量
	sql = "SELECT Total_Supply FROM COIN \
	       WHERE Name = '%s'" % Coin_Name

	try:
		# 执行SQL语句
		cursor.execute(sql)
		# 获取所有记录列表
		result = cursor.fetchone()
		print(result[0],type(result))
	except:
	   print ("Error: unable to fetch data")



	   
	time.sleep(3)


 
# 使用 execute() 方法执行 SQL，如果表存在则删除
#cursor.execute("DROP TABLE IF EXISTS TEST")
 
# 使用预处理语句创建表
'''
sql = """CREATE TABLE TEST (
         Coin_Name  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         lhuibin INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
 
cursor.execute(sql)
'''

# 关闭数据库连接
db.close()
print('爬取完成：成功%s,失败%s' %(count1,count2))
