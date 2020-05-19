import os
import shutil
import time
from datetime import datetime


def start_sort(folder_start, folder_finish):
    # Function to run basic logic from the graphical interface.
    file_list = []
    dir_dict = {}

    def folder_tree(folder_start):
        # Search for files in a given directory at all nesting levels.
        tree = os.walk(folder_start)
        for folder in tree:
            for file in folder[2]:
                full_path = os.path.join(folder[0], file)
                file_list.append(full_path)
                date = modification_date(full_path)
                new_tree(date, full_path)

    def modification_date(filename):
        # File creation date modifier.
        t = os.path.getmtime(filename)
        return datetime.fromtimestamp(t)

    def new_tree(date, full_path):
        # Creates a new tree directory of folders and files.
        year = str(date.year)
        if year in dir_dict:
            month = str(date.month)
            if month not in dir_dict[year]:
                dir_dict[year][month] = []
                dir_dict[year][month].append(full_path)
            else:
                dir_dict[year][month].append(full_path)
        else:
            dir_dict[year] = {}
            new_tree(date, full_path)

    def make_year(folder_finish, dir_dict):
        # Creates directories of years. Starts the function to create months.
        dir_year = os.listdir(folder_finish)
        for year in dir_dict:
            full_path_year = os.path.join(folder_finish, year)
            if year not in dir_year:
                os.mkdir(full_path_year)
                make_month(full_path_year, dir_dict[year])
            else:
                make_month(full_path_year, dir_dict[year])

    def make_month(full_path_year, dir_dict_year):
        # Creates a directory by months. Starts the file copying function.
        dir_month = os.listdir(full_path_year)
        for month in dir_dict_year:
            full_path_month = os.path.join(full_path_year, month)
            if month not in dir_month:
                os.mkdir(full_path_month)
                copy_past(full_path_month, dir_dict_year[month])
            else:
                copy_past(full_path_month, dir_dict_year[month])

    def copy_past(full_path_month, file_month_list):
        # Copies files from the root directory in the month of the new directory (according to the new tree).
        # Adds a time stamp to files with the same name to save both old and new files.
        for file_link in file_month_list:
            base_name = os.path.basename(file_link)
            if base_name not in os.listdir(full_path_month):
                shutil.copy2(file_link, full_path_month, follow_symlinks=True)
            elif modification_date(file_link) != modification_date(
                    os.path.join(full_path_month, base_name)):
                file_name, file_extension = os.path.splitext(base_name)
                current_time = datetime.now().strftime('%Y-%m-%d %H-%M-%S-%f')
                full_path_new_file = os.path.join(
                    full_path_month,
                    (file_name + current_time + file_extension))
                shutil.copy2(file_link,
                             full_path_new_file,
                             follow_symlinks=True)

    folder_tree(folder_start)
    make_year(folder_finish, dir_dict)