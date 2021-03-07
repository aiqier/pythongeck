# -*- coding: utf-8 -*-
import nose

from src.dateutil import datetime_to_timestamp_ms
from src.dateutil import datetime_to_timestamp_sec
from src.dateutil import now_datetime
from src.dateutil import datetime_to_strf
from src import dateutil

class TestDateUtil(object):

    def test_datetime_to_timestamp_ms(self):
        now = now_datetime()
        print datetime_to_timestamp_ms(now)
        print datetime_to_timestamp_sec(now)
        print datetime_to_strf(now, dateutil.YMD)
        print datetime_to_strf(now, dateutil.Y_M_D)
        print datetime_to_strf(now, dateutil.HMS)
        print datetime_to_strf(now, dateutil.H_M_S)
        print datetime_to_strf(now, dateutil.Y_M_D_H_M_S)
        print datetime_to_strf(now, dateutil.Y_M_D_H_M_S_F)
        print dateutil.timestamp_sec_to_datetime(datetime_to_timestamp_sec(now))
        print dateutil.timestamp_ms_to_datetime(datetime_to_timestamp_ms(now))
        print dateutil.generate_datetime(2012, 10, 12, 12, 15)
        assert "2019-10-17" == dateutil.strf_y_m_d_add_day("2019-10-15", 2)
        assert "2019-10-13" == dateutil.strf_y_m_d_deduct_day("2019-10-15", 2)
        print dateutil.is_same_day(now, now)
        print dateutil.today_y_m_d()
        print dateutil.yesterday_y_m_d()
        print dateutil.tomorrow_y_m_d()
        print dateutil.the_day_after_tomorrow_y_m_d()
        for d in dateutil.y_m_d_range_day("2019-10-13", 5):
            print d
        for d in dateutil.y_m_d_range("2019-10-13", "2019-10-18"):
            print d
