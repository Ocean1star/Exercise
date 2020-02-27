import requests
import re


def getHTMLText(url):
    try:
        kv={"User-Agent":"Mozilla/5.0","cookie":"t=3f29709c193e7a00dd4293a174b920c0; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; enc=BqRFrp3mLjOk5l1DeA%2Brhwzu2w35nN6lr1iPTWzWP6qcyY8x%2FgYKlAd3932A4I3dN0JCDZ%2FuoqHr%2FXmaQJ8lAw%3D%3D; cna=4PIRFlVCrBYCAbRUG17v7PBj; uc3=id2=UNN%2BxyVuPw0PEQ%3D%3D&lg2=UIHiLt3xD8xYTw%3D%3D&nk2=qhVQ%2By0Tr6cB7w%3D%3D&vt3=F8dBxdrJNdwOSw0C17s%3D; lgc=%5Cu751F%5Cu5E0C%5Cu6709%5Cu5FC3%5Cu4E36; uc4=nk4=0%40qC%2FJz4QaRN6rAAx%2Bdh6lZLcvCwlm&id4=0%40UgQ2gb47WiJWJ1wbotcTigsiQCXN; tracknick=%5Cu751F%5Cu5E0C%5Cu6709%5Cu5FC3%5Cu4E36; _cc_=WqG3DMC9EA%3D%3D; tg=0; mt=ci=-1_0; v=0; cookie2=116132d88cea4c41b38567e3d50f3732; _tb_token_=f3ab357b8df8b; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; JSESSIONID=84BA87C301C8F7BE0669209C74352FDF; _uab_collina=158056335424685649668612; x5sec=7b227365617263686170703b32223a223837373636666436333830396163396166306430373432383331646662386365434a6633316645464550622b73664c686c372b637267456144444d7a4d7a45344f5455794d6a59374d513d3d227d; uc1=cookie14=UoTUOqUNXzC3AA%3D%3D; l=cB_Bgx2gqDTT629ABOCwourza77OSIRfguPzaNbMi_5pL68_CQ7Oo4NE2FJ6cjWdtP8w4Tn8Nr29-etkidHx3mDgcGAN.; isg=BCMjBOvReT-adTbukne-lPhosmfNGLdaGBzJ7lWAMgL5lEG21ehHqgHGimSaNA9S"}
        r = requests.get(url,headers=kv,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return" "

def parsePage(ilt,html):
    try:
        plt = re.findall(r'"view_price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'"raw_title\"\:\".*?"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(" : ")[1])
            title = eval(tlt[i].split(" : ")[1])
            ilt.append([price,title])
    except:
        print(" ")

def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count = 0
    for g in ilt:
        count +=1
        print(tplt.format(count,g[0],g[1]))
    print(" ")

if __name__ == '__main__':
    goods = "书包"
    depath = 2
    start_url = "https://s.taobao.com/search?q="+goods
    infoList = []
    for i in range(depath):
        try:
            url = start_url+"&s="+str(44*i)
            html = getHTMLText(url)
            print(html)
            parsePage(infoList,html)
        except:
            continue
    printGoodsList(infoList)