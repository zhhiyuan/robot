import urllib.request
import urllib.parse
import re
from random import randint


def get_jokes():
    rule_joke = re.compile('<span id=\"text110\">([\w\W]*?)</span>')
    rule_url = re.compile('<a href=\"(.*?)\"target=\"_blank\" >')
    mainUrl = 'http://www.jokeji.cn'    #获取主页
    url = 'http://www.jokeji.cn/list.htm'

    req = urllib.request.urlopen(url)
    html = req.read().decode('gbk')     #编码形式
    urls = rule_url.findall(html)

    i = randint(0,20)
    url2 = urllib.parse.quote(urls[i])
    joke_url = mainUrl + url2
    req2 = urllib.request.urlopen(joke_url)
    html2 = req2.read().decode('gbk')
    joke = rule_joke.findall(html2)
    jokes = joke[0].split('<P>')
    length = len(jokes)
    # 格式化
    for i in range(length):
        jokes[i] = jokes[i].replace('<BR>', '\n')
        jokes[i] = jokes[i].replace('</P>', '')
    return jokes[randint(0,6)][2:]


if __name__ =='__main__':
    #有时候会返回空字符
    #获取速度不定
    #返回字符串
    print(get_jokes())