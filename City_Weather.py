'''
# coding=utf-8
import urllib
from city import city
import json


def search_weather(cityname):
    try:
        citycode = city[cityname]
    except:
        return ("找不到该城市")

    if citycode:
        try:
            url = "http://www.weather.com.cn/data/cityinfo/" + citycode + ".html"  # 构造网址
            content = urllib.urlopen(url).read()  # 读取网页源代码
            data = json.loads(content)  # 使用json库将字符转化为字典
            # print type(data)
            # print (content)
            res = data["weatherinfo"]  # 获取字典
            str_temp = ("%s :%s~%s") % (res["weather"], res["temp1"], res["temp2"])  # 格式化字符
            print(str_temp)
            # 输出天气信息
        except:
            return ("系统掉线了呢。。。。")


    '''
#coding=utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup
from city import city
def search_weather(cityname):
    try:
        citycode = city[cityname]
        try:
            resp = urlopen('http://www.weather.com.cn/weather/' + citycode + '.shtml')
            soup = BeautifulSoup(resp, 'html.parser')
            tagToday = soup.find('p', class_="tem")  # 第一个包含class="tem"的p标签即为存放今天天气数据的标签
            try:
                temperatureHigh = tagToday.span.string  # 有时候这个最高温度是不显示的，此时利用第二天的最高温度代替。
            except AttributeError as e:
                temperatureHigh = tagToday.find_next('p', class_="tem").span.string  # 获取第二天的最高温度代替

            temperatureLow = tagToday.i.string  # 获取最低温度
            weather = soup.find('p', class_="wea").string  # 获取天气

            return (cityname + ':\n' +'最低温度:' + temperatureLow + '\n' + '最高温度:' + temperatureHigh + '\n' + '天气:' + weather)
        except:
            return ('系统掉线了呢。。。')
    except:
        return ("中国找不到这个城市。。。")

#2018年4月22日17:17:10
if __name__ =='__main__':
    # cityname为存放整理后的文件夹路径
    # 结果会以字符串形式返回
    cityname=input('请输入你想查询天气的城市：')
    print(search_weather(cityname))