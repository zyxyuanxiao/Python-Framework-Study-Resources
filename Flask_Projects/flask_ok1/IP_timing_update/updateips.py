import http.client
import threading
# import datetime
from datetime import date, time, datetime, timedelta


# 工作
def ud():
    conn = http.client.HTTPConnection("127.0.0.1:5000")

    headers = {
        'cache-control': "no-cache",
        'postman-token': "81f15f78-c24f-366e-ead0-3ec4195e2abb"
    }

    conn.request("GET", "/user/get_ip", headers=headers)

    res = conn.getresponse()
    data = res.read()
    print('更新完成')
    # print(data.decode("utf-8"))
    # nt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # print(nt)


# Timer（定时器）是Thread的派生类，
# 用于在指定时间后调用一个方法。

# timer = threading.Timer(5, ud)
# timer.start()


# print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def runTask(func, day=0, hour=0, min=0, second=0):
    # 初始化时间
    now = datetime.now()
    strnow = now.strftime('%Y-%m-%d %H:%M:%S')
    print("初始化时间:", strnow)
    # 第一次下一次运行时间
    period = timedelta(days=day, hours=hour, minutes=min, seconds=second)  # 执行时间间隔
    next_time = now + period
    strnext_time = next_time.strftime('%Y-%m-%d %H:%M:%S')
    print("下一次运行时间:", strnext_time)
    while True:
        # 获取系统当前时间
        iter_now = datetime.now()
        iter_now_time = iter_now.strftime('%Y-%m-%d %H:%M:%S')
        if str(iter_now_time) == str(strnext_time):
            # 开始工作时间
            print("开始时间: %s" % iter_now_time)

            # 调用任务的功能
            func()
            print("执行任务...")

            # 获得下一次迭代时间
            iter_time = iter_now + period
            strnext_time = iter_time.strftime('%Y-%m-%d %H:%M:%S')
            print("迭代时间: %s" % strnext_time)

            # 继续下一个迭代
            continue


if __name__ == '__main__':
    # runTask(ud, day=0, hour=0, min=1,second=0)
    runTask(ud, second=3)
