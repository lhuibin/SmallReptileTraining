# coding=utf-8
"""根据搜索词下载百度图片
	教程来自于：https://blog.csdn.net/qq_37389133/article/details/79327948  """# 问题只会下载一页，出在页码列表不对，每次加载30张，页码应该是30,60,90网上加



import requests
from urllib.request import urlretrieve
import os

def Search(name,localpath,page):
    os.makedirs(localpath, exist_ok=True)  #这里创建文件夹路径，exist_ok=True 指如果有就不创建
    params = {
        'tn':'resultjson_com',
        'catename':'pcindexhot',
        'ipn':'rj',
        'ct':'201326592',
        'is':'',
        'fp':'result',
        'queryWord':'',
        'cl':'2',
        'lm':'-1',
        'ie':'utf-8',
        'oe':'utf-8',
        'adpicid':'',
        'st':'-1',
        'z':'',
        'ic':'0',
        'word':name,
        'face':'0',
        'istype':'2',
        'qc':'',
        'nc':'1',
        'fr':'',
        'pn':'0',
        'rn':'30'
        };
    params['pn'] = '%d' % page
    Request(params,localpath)
    return

def Request(param,path):
    searchurl  = 'http://image.baidu.com/search/avatarjson'   #百度图片
    response = requests.get(searchurl,params =param )         #传入请求参数
    json  = response.json()['imgs']    #每张图片有自己的下载路径
    for i in range(0,len(json)):
        filename = os.path.split(json[i]['objURL'])[1]
        Download(json[i]['objURL'],filename,path)
def Download(url,filename,filepath):
    path = os.path.join(filepath,filename)      #这里我们还是采用原来的图片
    try:                                                 #有些图片不知道为什么下载不了，所以这里用了try的方式
        urlretrieve(url,path)
        print('Downloading Images From ', url)
    except:
        print('Downloading None Images!')

#下载的主函数
if __name__ =='__main__':
    for i in range(30,3000,30): #这里可以方便的下载的图片数，每次json返回30张
      print(i)
      Search('汽车门店','M:/data/qixiu',i)    

