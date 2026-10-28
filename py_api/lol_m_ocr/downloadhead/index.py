
import json
import http.client
from PIL import Image
from  circle  import circleList

indexUrl = 'https://lolm.qq.com/main.html'
herolist = []
heroListURL ='game.gtimg.cn'
def getIndex ():
    conn = http.client.HTTPSConnection(indexUrl)
    conn.request("get", )
    res = conn.getresponse()
def getHeroList():
    headers = {
   'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)',
   'Accept': '*/*',
   'Host': 'game.gtimg.cn',
   'Connection': 'keep-alive'
    }
    conn = http.client.HTTPSConnection(heroListURL)
    conn.request("get",'/images/lgamem/act/lrlib/js/heroList/hero_list.js','',headers )
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
    jsondata = data.decode("utf-8")
    # print(json.dump(jsondata) )
    f = open('heroList.json', 'w',encoding='utf-8')
    f.write(jsondata)
    f.close()
    # with open("information.json",'r',encoding='utf-8') as f:
    #     model=json.load(f)
    # print(model)
# getHeroList()
def requestHeroAvatar(url,file_path):
    baseUrl =  url.split('game.gtimg.cn')[0]
    requestUrl = url.split('game.gtimg.cn')[1]
    print(requestUrl)
    conn = http.client.HTTPSConnection("game.gtimg.cn")
    payload = ''
    headers = {
      'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)',
      'Accept': '*/*',
      'Host': 'game.gtimg.cn',
      'Connection': 'keep-alive'
    }
    conn.request("GET", requestUrl, payload, headers)
    res = conn.getresponse()
    data = res.read()
    # print(data)
    with open(file_path, 'wb') as f:
      f.write(data)

# 输出名字
def getHeroName():
      with open("heroList.json",'r',encoding='utf-8') as f:
        model = json.load(f)
        heroList = model["heroList"]
        # print()
        for i in heroList:
            print(heroList[i]["name"])

def saveHeroAvatar():
    with open("heroList.json",'r',encoding='utf-8') as f:
        model = json.load(f)
        heroList = model["heroList"]
        num =0
        print(len(heroList))
        for i in heroList:
            num+=1
            url  = heroList[i]["avatar"]
            name = heroList[i]["name"]
            print(url,name)
            requestHeroAvatar(url,'./heroAvatar/{}.png'.format(name))
            # I = Image.open(url)
            # print(type(I))       #---><class 'PIL.JpegImagePlugin.JpegImageFile'>
            # print(I.size)        #--->(1280, 720)
            # I.show()
            # I.save('./heroAvatar./{}.png'.format(name))
            # if(num>1):
            #     break;


def main():
    # 获取英雄列表
    # getHeroList()
    #根据本地json储存官网头像 
    # saveHeroAvatar()
    # 切割本地成圆形
    # circleList()
    circleList('./heroAvatar/','./circleAvatar/')
main()  


# getHeroName()