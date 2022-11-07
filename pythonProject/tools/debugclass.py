import time
import arrow

'''
    时间转换
'''


# 默认为0，在返回当前时间戳，如果传时间则返回对应时间的时间戳
def unix_time(dt=0):

    timess = arrow.utcnow().timestamp()
    # 转换成时间数组
    timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
    # 转换成时间戳
    timestamp = time.mktime(timeArray)
    return timess


def local_time(timestamp):
    # 转换成localtime
    time_local = time.localtime(timestamp)
    # 转换成新的时间格式(2016-05-05 20:28:54)
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    return dt


if __name__ == '__main__':
    time_now = '2022-11-01 16:28:28'
    # unix_t = unix_time(time_now)
    unixtt  = unix_time(time_now)
    # local_t = local_time(unix_t)
    print(unixtt)

