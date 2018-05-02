from time import strftime,gmtime
def get_time():
    now_time=strftime("%Y-%m-%d %H:%M:%S",gmtime())
    return ('当前时间是'+now_time)

if __name__=='__main__':
    print(get_time())