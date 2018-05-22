import sys
from PyQt5.QtWidgets import QApplication,QWidget

if __name__=='__main__':
    app = QApplication(sys.argv)    #创建一个应用对象


    w = QWidget()   #控制用户界面的基本控件
    w.resize(250,150)   #窗口宽250，高150
    w.move(300,300) #把控件放置到屏幕坐标的(300, 300)的位置
    w.setWindowTitle('Simple')  #设置标题
    w.show()    #控件在桌面上显示

    sys.exit(app.exec_())