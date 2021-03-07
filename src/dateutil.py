# -*- coding: utf-8 -*-

import datetime
import time

YMD = "%Y%m%d"
Y_M_D = "%Y-%m-%d"
HMS = "%H%M%S"
H_M_S = "%H:%M:%S"

Y_M_D_H_M_S = "%Y-%m-%d %H:%M:%S"
Y_M_D_H_M_S_F = "%Y-%m-%d %H:%M:%S.%f"

def generate_datetime(*param):
    """
    生成 datetime
    :param param:
    :return:
    """
    return datetime.datetime(*param)

def datetime_to_timestamp_ms(dt):
    """
    date time对象转时间戳(毫秒)
    :return:
    """
    return int(time.mktime(dt.timetuple())) * 1000.0 + dt.microsecond / 1000.0

def datetime_to_timestamp_sec(dt):
    """
    date time对象转时间戳(秒)
    :return:
    """
    return int(time.mktime(dt.timetuple()))

def datetime_to_strf(dt, date_format):
    """
    date time对象转时间标准字符串
    具体格式：https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior
    :return:
    """
    return dt.strftime(date_format)

def timestamp_ms_to_datetime(ts):
    """
    时间戳(毫秒)转datetime对象
    :param ts:
    :return:
    """
    ltime = datetime.datetime.fromtimestamp(ts/1000)
    timeStr = ltime.strftime("%Y,%m,%d,%H,%M,%S,%f").split(',')
    timeInt = [int(i) for i in timeStr]
    return datetime.datetime(*timeInt)

def timestamp_sec_to_datetime(ts):
    """
    时间戳(秒)转datetime对象
    :param ts:
    :return:
    """
    ltime = time.localtime(ts)
    timeStr = time.strftime("%Y,%m,%d,%H,%M,%S", ltime).split(',')
    timeInt = [int(i) for i in timeStr]
    return datetime.datetime(*timeInt)

def strf_to_datetime(strf, date_format):
    """
    时间标准字符串转datetime
    :param strf:
    :return:
    """
    return datetime.datetime.strptime(strf, date_format)

def now_timestamp_ms():
    """
    返回当前时间戳(毫秒)
    :return:
    """
    return datetime_to_timestamp_ms(now_datetime())

def now_timestamp_sec():
    """
    返回当前时间戳(秒)
    :return:
    """
    return datetime_to_timestamp_sec(now_datetime())

def now_datetime():
    """
    返回datetime类型的当前时间
    :return:
    """
    return datetime.datetime.now()

def today_y_m_d():
    """
    当天 y-m-d eg: 2019-12-13
    :return:
    """
    return datetime_to_strf(now_datetime(), Y_M_D)

def yesterday_y_m_d():
    """
    昨天 y-m-d
    :return:
    """
    return strf_y_m_d_deduct_day(today_y_m_d(), 1)

def tomorrow_y_m_d():
    """
    明天 y-m-d
    :return:
    """
    return strf_y_m_d_add_day(today_y_m_d(), 1)

def the_day_after_tomorrow_y_m_d():
    """
    后天 y-m-d
    :return:
    """
    return strf_y_m_d_add_day(today_y_m_d(), 2)


def isweekend(dt):
    '''
    判断是否为周末
    1: Monday
    6: Saturday
    7: Sunday
    '''
    return dt.isoweekday() in (6, 7)

def is_valid_ymd(y_m_d):
    """
    是否是有效的 y-m-d时间
    :param ymd:
    :return:
    """
    try:
        datetime.datetime.strptime(y_m_d, Y_M_D)
    except ValueError:
        raise ValueError("Incorrect data format, should be yyyy-MM-DD")

def datetime_add_day(dt, days):
    return dt + datetime.timedelta(days=days)

def datetime_deduct_day(dt, days):
    return datetime_add_day(dt, -1 * days)

def strf_y_m_d_add_day(y_m_d, days):
    """
    y-m-d这样的时间格式加x天（eg:2012-02-12）
    :param strf:
    :param days:
    :return:
    """
    dt = datetime_add_day(strf_to_datetime(y_m_d, Y_M_D), days)
    return datetime_to_strf(dt, Y_M_D)

def strf_y_m_d_deduct_day(y_m_d, days):
    """
    y-m-d这样的时间格式减x天（eg:2012-02-12）
    :param y_m_d:
    :param days:
    :return:
    """
    return strf_y_m_d_add_day(y_m_d, -1 * days)

def is_same_day(d1, d2):
    """
    判断两天是否是同一天
    :param y_m_d1:
    :param y_m_d2:
    :return:
    """
    return d1.year == d2.year and d1.month == d2.month and d1.day == d2.day

def is_same_y_m_d(y_m_d1, y_m_d2):
    """
    判断两天是否是同一天
    :param y_m_d1:
    :param y_m_d2:
    :return:
    """
    return y_m_d1 == y_m_d2


def compare_datetime(d1, d2):
    """
    比较两个datetime 大小
    :param d1:
    :param d2:
    :return: d1 < d2 返回 -1， d1 == d2 返回 0， d1 > d2 返回 1
    """
    if d1 < d2:
        return -1
    elif d1 > d2:
        return 1
    else:
        return 0

def compare_strf(strf1, strf2, date_format):
    """
    比较格式化时间大小
    :param strf1:
    :param strf2:
    :param date_format:
    :return:
    """
    d1 = strf_to_datetime(strf1, date_format)
    d2 = strf_to_datetime(strf2, date_format)
    return compare_datetime(d1, d2)

def is_expire_day(strf, date_format):
    """
    判断一个格式化时间是否过期
    :param strf:
    :param date_format:
    :return:
    """
    return 1 == compare_datetime(strf_to_datetime(strf, date_format), now_datetime())

def datetime_range_day(start_datetime, r):
    """
    按照 range(day) 返回 datetime
    :param start_datetime:
    :param r:
    :return:
    """
    for i in range(r):
        yield datetime_add_day(start_datetime, r)

def y_m_d_range_day(y_m_d, r):
    """
    按照 range(day) 返回 ymd
    :param y_m_d:
    :param r:
    :return:
    """
    for i in range(r):
        yield strf_y_m_d_add_day(y_m_d, i)


def y_m_d_range(y_m_d_start, y_m_d_end):
    """
    返回两个时间段内的所有日期
    :param y_m_d_start:
    :param y_m_d_end:
    :return:
    """
    i = 0
    current_y_m_d = y_m_d_start
    while not is_same_y_m_d(current_y_m_d, y_m_d_end):
        current_y_m_d = strf_y_m_d_add_day(y_m_d_start, i)
        yield current_y_m_d
        i += 1