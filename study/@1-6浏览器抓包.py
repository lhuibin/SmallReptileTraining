
import requests,random,io,sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

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

url = 'http://www.sse.com.cn/disclosure/listedinfo/regular/'
formdata = {'jsonCallBack': 'jsonpCallback53822','reportType2': 'DQGG','reportType': 'ALL','beginDate': '2018-06-06','endDate': '2018-09-06','pageHelp.pageSize': 25,'pageHelp.pageCount': 50,'pageHelp.pageNo': 2,'pageHelp.beginPage': 2,'pageHelp.cacheSize': 1,'pageHelp.endPage': 21}

r = requests.post(url,data=formdata)

print(r.text)
'''
s = etree.HTML(r)
file = s.xpath('//*[@id="comments"]/ul/li/div[2]/p/span/text()')



# 使用pandas 保存数据
import pandas as pd
df = pd.DataFrame(file)
df.to_excel('pinglun.xlsx')



{"from":1,"size":20,"keyword":null,"catalogueId":"3","productFilter":{"brandIds":[],"properties":{}}}



'''