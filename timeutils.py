'''
Created on Apr 9, 2012

@author: peng
'''
import datetime
from calendar import monthrange

_EPOCH = datetime.datetime(1970, 1, 1)


def utc_timestamp(value=None):
    '''get utc timestamp'''
    if not value:
        value = datetime.datetime.utcnow()
    td = value - _EPOCH
    ts = (td.microseconds + (td.seconds + td.days * 24 * 3600) * 1e6) / 1e6
    return int(ts)


def get_last_week(value=None):
    '''get one week's date'''
    if not value:
        value = datetime.datetime.now()
    week_num = value.weekday()

    end_date = value - datetime.timedelta(days=week_num)
    days = 7
    week_days = []
    while days:
        end_date -= datetime.timedelta(days=1)
        week_days.append(end_date)
        days -= 1
    return week_days


def get_month_day_range(date_string, date_fromat):
    '''get month day range'''
    date = datetime.datetime.strptime(date_string, date_fromat)
    month_days = monthrange(date.year, date.month)[1]
    start_date = datetime.datetime(date.year, date.month, 1)
    end_date = start_date + datetime.timedelta(days=month_days - 1)
    return start_date, end_date
