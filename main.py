import requests  # 导入requests库
import json  # 导入json库
import re
import City_Weather,Move_File,SearchFile,jokes

key = '8c657754851549ceb9f474daf9694df7'  # 单引号里写你注册的的图灵机器人key


def main():
    while True:  # 主循环
        info = input(u'我>>')  # 输入对话信息
        if re.match(u"^([\u4e00-\u9fa5])+文件整理+[\u4e00-\u9fa5]", info) or re.match(u"^(文件整理)", info) or re.match(u"^([\u4e00-\u9fa5])+整理文件+[\u4e00-\u9fa5]", info) or re.match(u"^整理文件", info):
            print('小七>>好：')
            source=input('小七>>请输入你要整理的文件的路径:')
            des=input('小七>>请输入整理好你要存放的文件路径:')
            Move_File.move_file(source=source,destination=des)
        elif re.match(u"^([\u4e00-\u9fa5])+查找文件+[\u4e00-\u9fa5]", info) or re.match(u"^查找文件", info) or re.match(u"^文件查找", info) or re.match(u"^([\u4e00-\u9fa5])+文件查找+[\u4e00-\u9fa5]", info):
            print('小七>>好：')
            path = input('小七>>请告诉我你要查找的文件夹:')
            wanted = input('小七>>你要查找的文件拓展名是什么呢:')
            SearchFile.find_files(path,wanted)
        elif re.match(u"^([\u4e00-\u9fa5])+笑话+[\u4e00-\u9fa5]", info) or re.match(u"^([\u4e00-\u9fa5])+笑话", info):
            print('小七>>好呀好呀，最喜欢给主人讲笑话了：')
            print(jokes.get_jokes())
        elif re.match(u"^([\u4e00-\u9fa5])+市+[\u4e00-\u9fa5]",info):
            m=re.match(u"^([\u4e00-\u9fa5])+市",info)
            print('小七>> '+City_Weather.search_weather(m.group(0)[:-1]))  # 输出结果
        else:
            url = 'http://www.tuling123.com/openapi/api?key=' + key + '&info=' + info  # 组成url
            res = requests.get(url)  # 得到网页HTML代码
            res.encoding = 'utf-8'  # 防止中文乱码
            jd = json.loads(res.text)  # 将得到的json格式的信息转换为Python的字典格式
            print('小七>> ' + jd['text'])

if __name__=='__main__':
    main()