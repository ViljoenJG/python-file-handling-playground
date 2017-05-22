import datetime
import os

input_directory = 'input/'


def get_time_stamp(add_time=False, round_to=3):
    now = datetime.datetime.now()
    stamp = now.strftime('%Y-%m-%d')
    if add_time:
        return '%s %s_%s' % (stamp, now.strftime('%Hh%Mm%S'), now.strftime('%f')[0:round_to])
    return stamp

with open('output/%s.txt' % get_time_stamp(), 'a') as outfile:
    outfile.write('Merge start: %s\n' % get_time_stamp(True))
    file_list = os.listdir(input_directory)
    for filename in file_list:
        if filename.find('.txt') != -1:
            with open(input_directory + filename, 'r') as infile:
                outfile.write(infile.read() + '\n')
