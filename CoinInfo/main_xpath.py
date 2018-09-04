# -*-coding:utf-8-*-

# 抓取币种信息 使用xpath的方式

import requests,re,time
from lxml import etree
import os
import random
from urllib.request import urlretrieve
import pymysql

ua_list = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
        "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
]

user_agent=random.choice(ua_list)

# 获取数据函数
def get_data(url,user_agent):
	request=requests.get(url=url)
	request.encoding='uft-8'
	request.headers=user_agent
	response=request.text
	return response
coin_list = ['bitcoin', 'bitcoin-cash', 'decred', 'nano', 'litecoin', 'bitcoin-gold', 'bitcoin-diamond', 'dogecoin', 'dash', 'monero', 'zcash', 'verge', 'particl', 'zcoin', 'ethereum', 'eos', 'cardano', 'tezos', 'bytom', 'zilliqa', 'storiqa', 'syscoin', 'cybermiles', 'neo', 'icon', 'vite', 'loopring', 'loopring-neo', 'algorand', 'ontology', 'arcblock', 'wanchain', 'pallet', '0x', 'cybereits', 'loom-network', 'bluzelle', 'fabcoin', 'cortex', 'hitchain', 'sonm', 'poet', 'decentraland', 'scryinfo', 'credits', 'jibrel-network', 'investdigital', 'baic', '0xcert', 'dock', 'libra-credit', 'smartmesh', 'rightmesh', 'blockmesh','funfair','aelf']


# 打开数据库连接
db = pymysql.connect("localhost","root","lhuibin","mycoin" )
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
count1, count2=0,0

# 构造URL，可以利用list创建待查询的币种
for Coin_Name in coin_list:
	Coin_url="https://coinmarketcap.com/currencies/"+Coin_Name
	print(Coin_Name)
	# 抓取币种信息
	data = get_data(Coin_url, user_agent)
	s = etree.HTML(data)

	coin_price = s.xpath('//*[@id="quote_price"]/@data-usd')[0] #获取价格
	print(coin_price)

	for rank in s.xpath('/html/body/div[2]/div/div[1]/div[3]/ul/li[1]/span[2]'):#市值排名,不能抓取最后一个字符
		coin_rank = int(rank.text.split(' ')[-1])
		print(coin_rank)

	coin_MarketCap = s.xpath('/html/body/div[2]/div/div[1]/div[3]/div[2]/div[1]/div/span[1]/@data-usd')[0] # 流通市值,比特币的值是科学计数法
	print(coin_MarketCap)

	coin_Volume24h = s.xpath('/html/body/div[2]/div/div[1]/div[3]/div[2]/div[2]/div/span[1]/@data-usd')[0] # 24H交易量
	print(coin_Volume24h)

	coin_CirculatingSupply = s.xpath('/html/body/div[2]/div/div[1]/div[3]/div[2]/div[3]/div/span/@data-format-value')[0] # 流通量
	print(coin_CirculatingSupply)

	try:#防止没有数据时，出错
		coin_MaxSupply = s.xpath('/html/body/div[2]/div/div[1]/div[3]/div[2]/div[4]/div/span/@data-format-value')[0] # 总量
		print(coin_MaxSupply)
	except:
		print(Coin_Name+'没有总量数据')
'''
	
	# SQL 查询总量
	sql_Total = "SELECT Total_Supply FROM COIN \
	       WHERE Name = '%s'" % Coin_Name

	try:
		# 执行SQL语句
		cursor.execute(sql_Total)
		# 获取所有记录列表
		result_Total = cursor.fetchone()
		coin_TotalSupply = int(result_Total[0]) 

	except:
	   print ("Error: unable to fetch Total_Supply")
	
	coin_MarketCap = coin_price * coin_CirculatingSupply
	coin_TotalCap = coin_price * coin_TotalSupply
	coin_CirculatingRatio = coin_CirculatingSupply/coin_TotalSupply

	# SQL 查询语句
	sql = "SELECT * FROM COIN \
	       WHERE Name = '%s'" % Coin_Name
	try:
		# 执行SQL语句
		cursor.execute(sql)
		# 获取所有记录列表
		result = cursor.fetchone()
		if result==None:
		# SQL 插入语句
			sql = """INSERT INTO COIN VALUES (Name='%s',Rank='%s', Price='%s', Market_Cap='%s', Circulating_Supply='%s',Total_Cap='%s',Circulation_Ratio='%s')"""%(Coin_Name,coin_rank,coin_price,coin_MarketCap,coin_CirculatingSupply,coin_TotalCap,coin_CirculatingRatio)
			update_info="增加"
		else:
		# SQL 更新语句

			sql = "UPDATE COIN SET Rank='%s',Price='%s',Market_Cap='%s',Circulating_Supply='%s',Total_Cap='%s',Circulation_Ratio='%s' where Name='%s'" %(coin_rank,coin_price,coin_MarketCap,coin_CirculatingSupply,coin_TotalCap,coin_CirculatingRatio,Coin_Name)
			update_info="更新"
	except:
	   print ("Error: unable to fetch data")


	try:
	   # 执行sql语句coin
	   cursor.execute(sql)
	   # 提交到数据库执行
	   db.commit()
	   count1=count1+1
	   print(Coin_Name,update_info,'成功')
	except:
	   # 如果发生错误则回滚
	   db.rollback()
	   count2=count2+1
	   print(Coin_Name,update_info,'失败')
	   
	time.sleep(3)

'''
 
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
#print('爬取完成：成功%s,失败%s' %(count1,count2))



