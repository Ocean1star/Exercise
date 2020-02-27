import bs4
import requests
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return" "
def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):#是否是bs4的标签
            tds = tr("td")#所有标签存储为列表tds
            ulist.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string])
    return ulist

def printUnivList(ulist,num):
    tplt = "{0:^5}\t{1:{4}^10}\t{2:^6}\t{3:^5}"
    print(tplt.format("排名","学校名称","地区","总分",chr(12288)))
    for i in range(num):
        u=ulist[i]
        print(tplt.format(u[0], u[1],u[2],u[3],chr(12288)))
    print("Suc"+str(num))

if __name__ == '__main__':
    uinfo = []
    url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2019.html"
    html = getHTMLText(url)
    ulist=fillUnivList(uinfo,html)
    printUnivList(ulist,100) #100所大学排名信息
