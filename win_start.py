'''
This script should prepare PC for work.
1) Waits for the system to boot up;
2) Starts all necessary programs and waits for them to start;
3) Starts the clicker which should already start everything inside the programs.
The file with the script should be in the same place where all the programs that need to be started (links, shortcuts, programs, scripts) are collected.
'''

import os
from time import sleep
from psutil import cpu_percent, disk_io_counters, process_iter, Process

# Getting a list of files and a directory address.
file_list = os.listdir()
link_dir = os.getcwd()


def busy(func):
    # The function waits for PC to enter the idle state checking every 10 seconds reading\writing to disk and
    # the percentage of load on the CPU. If is not being reading\writing and the CPU load is less than 5%, it starts
    # the execution of the function transferred to it then stops.
    while True:
        # The number is a reading + writing index.
        busytime = disk_io_counters().read_time + disk_io_counters().write_time
        sleep(10)
        if (busytime == disk_io_counters().read_time + disk_io_counters().write_time) and (cpu_percent(interval=1) < 5):
            return func()


def start_prog():
    # The function searches for files to start, creates full addresses and runs them.
    # Creating a list of file extensions it's looking for.
    extension = ['lnk', 'url']
    # Exceptions that should not be started in this function.
    excluding = ['pilot', ]
    # Fill in the list with the full addresses of the files to run.
    for link in file_list:
        file_name, file_extension = os.path.splitext(link)
        if (file_extension.lower()[1:] in extension) and (file_name not in excluding):
            os.startfile(link_dir + '\\' + link)
            file_list.remove(link)


def start_click():
    # The function searches for files to start, creates full addresses and runs them.
    extension = ['lnk', ]
    # Fill in the list with the full addresses of the files to run.
    for link in file_list:
        file_name, file_extension = os.path.splitext(link)
        if file_extension.lower()[1:] in extension:
            os.startfile(link_dir + '\\' + link)


def process_killer():
    # The function kills the unnecessary process. So far, in person.
    for i in process_iter(['pid', 'name']):
        if i.name() == 'browser.exe':
            Process(i.pid).kill()


busy(start_prog)
busy(start_click)
busy(process_killer)
