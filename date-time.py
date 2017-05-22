import datetime
import time

r"""
This script creates an empty file.
- The name of the file includes a time stamp.
"""

output = 'output/'
ext = '.txt'


def get_time_stamp():
    now = datetime.datetime.now()
    ms = now.strftime('-%f')[0:4]
    return now.strftime('%Y-%m-%d %Hh%mm%S') + ms


# Creates an empty file
def create_file(name):
    """This function creates an empty file."""
    name = name + ' ' + get_time_stamp()
    with open(output + name + ext, 'w') as file:
        file.write("")

for i in range(5):
    create_file('sample' + str(i+1))
    time.sleep(1)
