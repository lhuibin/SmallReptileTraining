import requests,io,sys
r = requests.get('https://book.douban.com/subject/1084336/comments/').text

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') #改变标准输出的默认编码

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