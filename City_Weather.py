import json, sys, requests

# 输入地点
def search_weather(city):
    # 下载天气JSON
    weatherJsonUrl = "http://wthrcdn.etouch.cn/weather_mini?city=%s" % (city)
    response = requests.get(weatherJsonUrl)
    try:
        response.raise_for_status()
        # 将json文件格式导入成python的格式
        weatherData = json.loads(response.text)
        w = weatherData['data']
        date_a = (w['forecast'][0]['date'])  # 日期
        highTemp = (w['forecast'][0]['high'])  # 最高温度
        lowTemp = (w['forecast'][0]['low'])  # 最低温度
        weather = (w['forecast'][0]['type'])  # 天气
        str = ''
        str = str + ("温度：最" + lowTemp + '，最' + highTemp + '\n') + ("天气：" + weather) + (
        "\n今日着装：" + w['ganmao']) + ("\n当前温度：" + w['wendu'] + "℃")
        return str
    except:
        return ("网址请求出错")

if __name__ == '__main__':
    city = input("请输入天气地点：")
    print(search_weather(city))