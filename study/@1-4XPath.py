# xpath用法整理：https://blog.csdn.net/u013332124/article/details/80621638


import requests
from lxml import etree

url = 'https://book.douban.com/subject/1084336/comments/'
r = requests.get(url).text

s = etree.HTML(r)
#从浏览器复制第一条评论的Xpath
for i in s.xpath("//*[@class='comment-content']/span"):
	print(i.text+"|")
'''
//*[@id="comments"]/ul/li[5]/div[2]/p
#从浏览器复制第二条评论的Xpath
print(s.xpath('//*[@id="comments"]/ul/li[2]/div[2]/p/text()'))
#从浏览器复制第三条评论的Xpath
print(s.xpath('//*[@id=“comments”]/ul/li[3]/div[2]/p/text()'))

#掌握规律，删除li[]的括号，获取全部短评
print(s.xpath('//*[@id=“comments”]/ul/li/div[2]/p/text()'))

#手写Xpath获取全部短评
print(s.xpath('//div[@class="comment"]/p/text()'))
'''