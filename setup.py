import json,requests,re
from PyQt5.QtWidgets import *
from UI import Ui_MainWindow
import Move_File,SearchFile,jokes,City_Weather
import easygui as eg

key = '8c657754851549ceb9f474daf9694df7'  # 图灵机器人key


class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,*args,**kwargs):
        super(MainWindow,self).__init__(*args,**kwargs)
        self.setupUi(self)
        self.srcTextEdit.setReadOnly(True)
        self.translateButton.pressed.connect(self.getmain)
        self.show()

    def getmain(self):
        info = self.destTextEdit.toPlainText()
        text=self.Function(info)
        self.srcTextEdit.setPlainText(text)

    def Function(self,info):
        if re.match(u"^([\u4e00-\u9fa5])+你会干什么+[\u4e00-\u9fa5]", info) or re.match(u"^你会干什么",
            info) or re.match(u"^([\u4e00\u9fa5])+你会干什么", info) or re.match(u"^你会干什么+[\u4e00-\u9fa5]", info):
            msg = '小七>>\n我会的可多啦！\n你可以叫我帮你整理文件、查找文件、讲笑话、查天气...\n我还会许多东西呢!\n来和我聊天吧！'
            return msg
        elif re.match(u"^([\u4e00-\u9fa5])+文件整理+[\u4e00-\u9fa5]", info) or re.match(u"^(文件整理)", info) or re.match(
                u"^([\u4e00-\u9fa5])+整理文件+[\u4e00-\u9fa5]", info) or re.match(u"^整理文件", info):
            eg.msgbox(msg='请选择你要整理的文件夹的路径', title='小七-文件整理')
            source=QFileDialog.getExistingDirectory()  #打开文件夹
            eg.msgbox(msg='请选择要保存的文件夹的路径', title='小七-保存文件')
            des = QFileDialog.getExistingDirectory()
            Move_File.move_file(source=source, destination=des)
            return '文件整理好了呢！'
        elif re.match(u"^([\u4e00-\u9fa5])+查找文件+[\u4e00-\u9fa5]", info) or re.match(u"^查找文件", info) or re.match(
                u"^文件查找", info) or re.match(u"^([\u4e00-\u9fa5])+文件查找+[\u4e00-\u9fa5]", info):
            path = QFileDialog.getExistingDirectory()   #打开文件夹
            wanted = eg.enterbox(msg='你要查找的文件拓展名是什么呢:', title='小七-查找文件')
            return '小七>>\n你要找的文件有没有在下面呀：\n' + SearchFile.find_files(path, wanted)
        elif re.match(u"^([\u4e00-\u9fa5])+笑话+[\u4e00-\u9fa5]", info) or re.match(u"^([\u4e00-\u9fa5])+笑话", info):
            return '小七>\n好呀好呀，最喜欢给主人讲笑话了：\n' + jokes.get_jokes()
        elif re.match(u"^([\u4e00-\u9fa5])+市+[\u4e00-\u9fa5]", info):
            m = re.match(u"^([\u4e00-\u9fa5])+市", info)
            return ('小七>>\n ' + City_Weather.search_weather(m.group(0)[:-1]))  # 输出结果
        else:
            url = 'http://www.tuling123.com/openapi/api?key=' + key + '&info=' + info  # 组成url
            res = requests.get(url)  # 得到网页HTML代码
            res.encoding = 'utf-8'  # 防止中文乱码
            jd = json.loads(res.text)  # 将得到的json格式的信息转换为Python的字典格式
            return ('小七>> \n' + jd['text'])

if __name__ == '__main__':
    app=QApplication([])
    window=MainWindow()
    app.exec_()