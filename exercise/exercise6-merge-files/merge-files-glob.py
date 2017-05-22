import datetime
import glob2

input_directory = 'input/'


def get_time_stamp(add_time=False, round_to=3):
    now = datetime.datetime.now()
    stamp = now.strftime('%Y-%m-%d')
    if add_time:
        return '%s %s_%s' % (stamp, now.strftime('%Hh%Mm%S'), now.strftime('%f')[0:round_to])
    return stamp

file_names = glob2.glob(input_directory + '*.txt')

with open('output/result %s.txt' % get_time_stamp(True), 'a') as outfile:
    for filename in file_names:
        with open(filename, 'r') as infile:
            outfile.write(infile.read() + '\n')
