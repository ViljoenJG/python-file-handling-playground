import datetime
import time

r"""
This script creates an empty file.
- The name of the file includes a time stamp.
"""

output = 'output/'
ext = '.txt'


def get_time_stamp(addTime):
    now = datetime.datetime.now()
    stamp = now.strftime('%Y-%m-%d')
    if addTime:
        return '%s %s_%s' % (stamp, now.strftime('%Hh%Mm%S'), now.strftime('%f')[0:3])
    return stamp


def create_file(name):
    with open(output + name + ext, 'a') as file:
        file.write('>> Started at: %s\n' % get_time_stamp(True))
        for i in range(5):
            file.write('timestamp%d: %s\n' % (i+1, get_time_stamp(True)))
            time.sleep(1)
        file.write('\n')

create_file('date-time ' + get_time_stamp(False))
