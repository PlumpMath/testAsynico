# coding: utf-8
import time
import functools
def follow(thefile):
    # thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line
def coroutine(func):
    @functools.wraps(func)
    def f(*args,**kwargs):
        cr = func(*args,**kwargs)
        cr.__next__()
        return cr
    return f

@coroutine
def grep(pattern):

    print ("looking for %s"%pattern)
    while True:
        line = (yield )
        if pattern in line:
            print(line)

logfile = open("/home/guo/mygit/readme.txt")
loglines = follow(logfile)
pylines = grep("is")
# for line in pylines:
#     print(line)
# follow(logfile)
# pylines.__next__()
pylines.send('he is my bestfriends')
pylines.send('he was my bestfriends')
pylines.send('his father is my bestfriends')