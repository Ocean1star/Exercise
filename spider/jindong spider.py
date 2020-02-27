import requests



def getHTMLText(url):
    try:
        #请求url链接，设置响应时间30
        r= requests.get(url,timeout=30)
        #看是否是200
        r.raise_for_status()
        #解码正确
        r.encoding=r.apparent_encoding
        #解码内容
        return r.text
    except:
        return "404"

def gettext(url):
    try:
        kv={"user-agent":"Mozilla/5.0"}
        r=requests.get(url,headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return (r.text[1000:2000])
    except:
        return 404

def select_info(url):
    keyword = "Python"
    try:
        kv={"q":keyword}
        r = requests.get(url,params=kv)
        print(r.request.url)
        r.raise_for_status()
        print(len(r.text))
    except:
        print(404)

def select_info_2(url):
    keyword = "Python"
    try:
        kv={"wd":keyword}
        r = requests.get(url,params=kv)
        print(r.request.url)
        r.raise_for_status()
        print(len(r.text))
    except:
        print(404)

#图片的爬取存储
import os
def get_picture(url,root):
    path=root+url.split("/")[-1]
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url)
            with open(path,"wb") as f:
                f.write(r.content)
                f.close()
                print("Save all")
        else:
            print("The file is existed")
    except:
        print("Filed")

#查询ip地址
def select_ip(ip):
    url = "http://www.ip138.com/iplookup.asp?ip="
    try:
        r = requests.get(url+ip)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text[7000:8000])
    except:
        print(404)


#标签树的上行遍历
from bs4 import BeautifulSoup
def soup(demo):
    soup = BeautifulSoup(demo,"html.parser")
    for parent in soup.a.parents:
        if parent is None:
            print(parent)
        else:
            print(parent.name)

if __name__ == '__main__':
    #url=("http://item.jd.com/2967929.html")
    # url=("http://www.baidu.com/s")
    # url_1=("http://www.so.com/s")
    # url=("https://www.amazon.cn/gp/product/B01M8L5Z3Y")
    # print(gettext(url))
    # select_info(url)
    # select_info_2(url_1)
    # url="http://cache.tv.qq.com/qqplayerout.swf?vid=b0507n7c508"
    # path="F://pics//"
    # get_picture(url,path)
    soup(getHTMLText("http://python123.io/ws/demo.html"))


