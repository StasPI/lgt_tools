'''
Clearing old files (by specified extensions) in specified directories (folders).
'''


import os
import time
import datetime


# Extensions to be removed and the paths to be followed by the operation.
extension = ['pdf', 'xlsx', 'jpeg', 'xls']
file_dir = [r'A:\test', r'A:\test1']
# Getting the date of the current.
# Countdown 30 days ago (maximum period of desired file storage).
# Getting a meaning from the beginning of an era.
now_date = datetime.datetime.now()
nubmer_days_ago = now_date - datetime.timedelta(days=30)
control_time = datetime.datetime.timestamp(nubmer_days_ago)

for path_dir in file_dir:
    all_file_dir = os.listdir(path_dir)
    for file in all_file_dir:
        # Getting the file extension.
        file_name, file_extension = os.path.splitext(file)
        if file_extension[1:].lower() in extension:
            full_path = path_dir + '\\' + file
            # Getting a value from the beginning of the era of the file being checked.
            file_time = os.path.getmtime(full_path)
            if control_time > file_time:
                os.remove(full_path)
