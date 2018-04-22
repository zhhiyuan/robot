'''

#实现桌面整理功能
#根据文件后缀名整理桌面
#2018年4月21日17:30:33

import os
import time
#传递文件名，返回其后缀名
def file_extension(path):
  return os.path.splitext(path)[1]

#文件后缀名的文件夹是否存在，存在，则返回false，否则返回true
def is_exten_exit(filename):
    extension = file_extension(filename)

def timestamp():
    tp = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time()))
    return tp

def collectSet(f):
    a = (f != 'desktop.ini' and f != 'clearDTP.py' and f != 'Archive.py' and 'box' not in f and 'archive' not in f)
    return a

try:
    f = open('dir1.txt','r')
    dir1=f.readline()
    f.close()
except:
    dir1=input('请设置桌面路径：')
    f = open('dir1.txt','w')
    f.write(dir1)
    f.close()
finally:
    marks = '整理的文件'
    targetDir = timestamp() + marks  # 整理后的文件名
    pan = os.path.exists(dir1 + os.sep + targetDir)
    if not pan:
        os.mkdir(targetDir)

    for f in os.listdir(dir1):
        collectSet(f)
        sCmd = ' '.join(['move', f, targetDir + os.sep])  # 移动文件夹指令
        if os.system(sCmd) == 0:  # 生成文件夹指令
            exit(0)


'''
import os
import shutil
import sys

class Pyorg:
	def organize(self,source,destination):
		curr_dir = source
		files = os.listdir(curr_dir)

		if len(files) == 0:
			return ("整理的文件夹不存在或没有可以整理的文件！")
		for file in files:
			ext = file.split('.')[-1]
			dest = destination + '/' + ext
			if not os.path.exists(dest):
				os.makedirs(dest)
			if not os.path.isdir(file):
				shutil.move(curr_dir + '/' + file, dest)
		return ('文件整理成功！')



def move_file(destination,source):
	if destination == '--curr':
		destination = os.getcwd()
	elif not os.path.exists(destination):
		return ("存放的文件夹不存在！")
	pyorg = Pyorg()
	pyorg.organize(source,destination)

#2018年4月22日16:49:50
if __name__ == '__main__':
	#destination为存放整理后的文件夹路径
	#source将要整理的文件夹
	#结果会以字符串形式返回
	source=input('请输入想要整理的文件夹路径：')
	destination = input('请输入想要存放的文件夹路径：')
	print(move_file(source,destination))
