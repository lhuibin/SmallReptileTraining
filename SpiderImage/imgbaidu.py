# coding=utf-8
"""根据搜索词下载百度图片
	教程来自于：https://blog.csdn.net/qq_34209701/article/details/72638966  """ # 问题是遇到不能下载的图片就停止了。


import requests
import os
 
def getPages(keyword,pages):
    params = []
    for i in range(30, 30*pages+30, 30):
        params.append({
                      'tn': 'resultjson_com',
                      'ipn': 'rj',
                      'ct': 201326592,
                      'is': '',
                      'fp': 'result',
                      'queryWord': keyword,
                      'cl': 2,
                      'lm': -1,
                      'ie': 'utf-8',
                      'oe': 'utf-8',
                      'adpicid': '',
                      'st': -1,
                      'z': '',
                      'ic': 0,
                      'word': keyword,
                      's': '',
                      'se': '',
                      'tab': '',
                      'width': '',
                      'height': '',
                      'face': 0,
                      'istype': 2,
                      'qc': '',
                      'nc': 1,
                      'fr': '',
                      'pn': i,
                      'rn': 30,
                      'gsm': '1e',
                      '1488942260214': ''
                  })
    url = 'https://image.baidu.com/search/acjson'
    urls = []
    for i in params:
        urls.append(requests.get(url, params=i).json().get('data'))
    return urls
 
def getImg(dataList, localPath):
 
    if not os.path.exists(localPath):
        os.mkdir(localPath)
 
    try:
        x = 0
        for list in dataList:
            for i in list:
                if i.get('thumbURL') != None:
                    print('正在下载：%s' % i.get('thumbURL'))
                    ir = requests.get(i.get('thumbURL'))
                    open(localPath + '%d.jpg' % x, 'wb').write(ir.content)
                    x += 1
        print('图片下载完成')
    except Exception:
        print("图片下载失败")
 
if __name__ == '__main__':
    dataList = getPages('汽修店', 3)
    getImg(dataList, 'D:/images/')



