import time, datetime
from datetime import datetime, timedelta, date

# 获取当前时间下最近7天的第一天的【时间戳+000】

    # 获取当前时间
# time_now = datetime.now().strftime('%Y-%m-%d')
#
# print(time_now)
#
# now =datetime.now() + timedelta(days=-6)
# print(now)
#
# day_time = int(time.mktime(datetime.now().timetuple())+)
# print(day_time)

# time_now = datetime.now()
# timeEnd = time_now + timedelta(days=-6)
# un_timeEnd = str(time.mktime(timeEnd.timetuple())).split('.')[0]+"000"
# print(un_timeEnd)

# today = datetime.today()
# print(today)
# today_time = int(time.mktime(today.timetuple()))
# print(today_time)

now_time = int(time.time())
day_time = now_time - now_time % 86400 + time.timezone
print(day_time)
