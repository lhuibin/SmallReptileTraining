import requests,io,sys,pandas
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') #改变标准输出的默认编码

'''
r = requests.get('https://book.douban.com/subject/1084336/comments/').text

from bs4 import BeautifulSoup
soup = BeautifulSoup(r,'lxml')
pattern = soup.find_all('p','comment-content')
for item in pattern:
	print(item.text)

import pandas
comments =[]
for item in pattern:
	comments.append(item.text)
df = pandas.DataFrame(comments)
df.to_csv('comments.csv')
'''

#定义函数
def getHTMLText(url):
	try:
		r = requests.get(url,timeout=20) #设置超时时间
		r.raise_for_status()
		r.encoding = 'utf8'
		return r.text
	except: #异常处理
		return '产生异常'

if __name__ == '__main__':
	url = 'https://book.douban.com/subject/1084336/comments/'
	
	soup = BeautifulSoup(getHTMLText(url),'lxml') #调用函数
	pattern = soup.find_all('p','comment-content')

	comments = []
	for item in pattern:
		comments.append(item.text)
	df = pandas.DataFrame(comments)
	df.to_csv('comments.csv')	
