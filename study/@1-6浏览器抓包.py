
import requests
from lxml import etree

url = 'https://book.douban.com/subject/1084336/comments/'
r = requests.get(url).text

s = etree.HTML(r)
file = s.xpath('//*[@id="comments"]/ul/li/div[2]/p/span/text()')

'''#使用with open()新建对象 写入数据
with open('pinglun.txt', 'a', encoding='utf-8') as f:#使用with open()新建对象f
	for i in file:
		print(i)
		f.write(i)#写入数据，文件保存在当前工作目录'''


# 使用pandas 保存数据
import pandas as pd
df = pd.DataFrame(file)
df.to_excel('pinglun.xlsx')


#import os
#os.getcwd()#得到当前工作目录
#os.chdir()#修改当前工作目录，括号中传入工作目录的路径
#参数	用法
#r	只读。若不存在文件会报错。
#w	只写。若不存在文件会自动新建。
#a	附加到文件末尾。
#rb, wb, ab	操作二进制



'''
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(6,3)) #创建随机值并保存为DataFrame结构
print(df.head())
df.to_csv('numpppy.csv')

#df.to_excel('文件名.xlsx', sheet_name = 'Sheet1') #其中df为DataFrame结构的数据，sheet_name = 'Sheet1'表示将数据保存在Excel表的第一张表中
#pd.read_excel('文件名.xlsx', 'Sheet1', index_col=None, na_values=['NA']) #从excel中读取数据
'''

{"from":1,"size":20,"keyword":null,"catalogueId":"3","productFilter":{"brandIds":[],"properties":{}}}
