
import requests,random,io,sys,time
import pandas as pd
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

from lxml import etree
ua_list = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
        "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
]
user_agent=random.choice(ua_list)
headers = {
	'content-security-policy': "default-src * blob:; img-src * data: blob:; connect-src * wss:; frame-src 'self' *.zhihu.com weixin: *.vzuu.com getpocket.com note.youdao.com safari-extension://com.evernote.safari.clipper-Q79WDW8YH9 zhihujs: captcha.guard.qcloud.com; script-src 'self' blob: *.zhihu.com res.wx.qq.com 'unsafe-eval' unpkg.zhimg.com unicom.zhimg.com captcha.gtimg.com captcha.guard.qcloud.com pagead2.googlesyndication.com i.hao61.net; style-src 'self' 'unsafe-inline' *.zhihu.com unicom.zhimg.com captcha.gtimg.com",
	'cookie': '_zap=84305856-48d5-4195-8b6a-2620773be50e; _xsrf=6739a3d4-2d6a-495a-99fa-4c4f5a8802bf; d_c0="AKDjMIrmKw6PTrq_4PO1yAwJr97hTXPxQT4=|1536244284"; tgw_l7_route=53d8274aa4a304c1aeff9b999b2aaa0a; capsion_ticket="2|1:0|10:1536245766|14:capsion_ticket|44:ZWQwMWM2ODI0ZWJkNGQ0OWJhMjVhYTJmNDVmOTYxOGU=|433d974936fb88318ee39e4b85e41d1d75f7f2c518cd5efadabeb83de85fdfcd"; z_c0="2|1:0|10:1536245803|4:z_c0|92:Mi4xWFdDbUF3QUFBQUFBb09Nd2l1WXJEaVlBQUFCZ0FsVk5LbzUtWEFEMzlNbHhvOVljYzFRZWc1N0FNNWRENlViOVd3|2775f184b37aa649945dc5e436e358b1a031ea77bd83f5eada5dcca296511324"; unlock_ticket="AEBAN7K7ygomAAAAYAJVTTNHkVunCHtKnUYuEDCPLYI_RIFmfxLR9A=="',
	'set-cookie': 'tgw_l7_route=53d8274aa4a304c1aeff9b999b2aaa0a; Expires=Thu, 06-Sep-2018 15:05:29 GMT; Path=/',
	#'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
	'user-agent': user_agent,
}
file = []

def get_data(page):
	for i in range(page):
		url='https://www.zhihu.com/api/v4/members/excited-vczh/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset={}&limit=20'.format(i*20)

		r = requests.get(url,headers=headers).json()['data']

		print('正在爬取%s' % str(i+1))
		file.extend(r)
		time.sleep(2)
	'''
	s = etree.HTML(r)
	file = s.xpath('//*[@id="comments"]/ul/li/div[2]/p/span/text()')
'''


#使用pandas 保存数据
if __name__ == '__main__':
	get_data(2)
	df = pd.DataFrame.from_dict(file)
	df.to_excel('pinglun.xlsx')





