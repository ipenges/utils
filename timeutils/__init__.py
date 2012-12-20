'''
Created on Apr 9, 2012

@author: peng
'''
from datetime import datetime

_EPOCH = datetime(1970, 1, 1)


def utc_timestamp(value=None):
    if not value:
        value = datetime.utcnow()
    td = value - _EPOCH
    ts = (td.microseconds + (td.seconds + td.days * 24 * 3600) * 1e6) / 1e6
    return int(ts)
