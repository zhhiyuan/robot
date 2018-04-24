import os
import shutil

def organize(source,destination):
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
	if destination == '--curr':	#获取目的地址
		destination = os.getcwd()
	elif not os.path.exists(destination):
		return ("存放的文件夹不存在！")
	return organize(source, destination)

#2018年4月22日16:49:50
if __name__ == '__main__':
	#destination为存放整理后的文件夹路径
	#source将要整理的文件夹
	#结果会以字符串形式返回
	source=input('请输入想要整理的文件夹路径：')
	destination = input('请输入想要存放的文件夹路径：')
	print(move_file(source,destination))
