import os
import time
from datetime import datetime
from xml.etree import ElementTree as ET

from PIL import Image


def twin_go(folder_start, folder_finish):
    # Function to run basic logic from the graphical interface.
    meta_list = []
    key_list = []
    finish_list = []
    image_dict = {}

    def folder_tree(folder_start):
        # Bypass the directory tree. Collecting in the dictionary key - full path,
        # value - metadata (for all files that match) . Collecting into the Metadata List.
        for dr in os.listdir(folder_start):
            full_path = os.path.join(folder_start, dr)
            if os.path.isfile(full_path):
                base_name = os.path.basename(full_path)
                if image_check(base_name):
                    date = modification_date(full_path)
                    image_data = image_metadata(full_path)
                    size = os.path.getsize(full_path)
                    up_list = [
                        base_name,
                        size,
                        date.year,
                        date.month,
                        date.day,
                        image_data
                    ]
                    up_string = ''.join(map(str, up_list))
                    image_dict[full_path] = up_string
                    meta_list.append(up_string)
                elif image_check_optional(base_name):
                    date = modification_date(full_path)
                    size = os.path.getsize(full_path)
                    up_list = [
                        base_name,
                        size,
                        date.year,
                        date.month,
                        date.day,
                    ]
                    up_string = ''.join(map(str, up_list))
                    image_dict[full_path] = up_string
                    meta_list.append(up_string)
            elif os.path.isdir(full_path):
                folder_tree(full_path)

    def modification_date(filename):
        t = os.path.getmtime(filename)
        return datetime.fromtimestamp(t)

    def image_metadata(image):
        # Image size in pixels.
        im = Image.open(image)
        return im.size

    def image_check(base_name):
        extension = (
            '.jpg',
            '.nef',
            '.cr2',
            '.dng',
            '.eps',
            '.png',
            '.pxr',
            '.tif',
        )
        file_name, file_extension = os.path.splitext(base_name)
        return file_extension in extension

    def image_check_optional(base_name):
        extension = (
            '.pdf',
            '.arw',
            '.rw2',
            '.ai',
            '.dcm',
            '.raw',
        )
        file_name, file_extension = os.path.splitext(base_name)
        return file_extension in extension

    def get_key(val):
        # Key list creation for identical files:
        for key, value in image_dict.items():
            if val == value:
                key_list.append(key)

    def full_path_name_file(file_extension):
        current_time = datetime.now().strftime('%Y-%m-%d %H-%M')
        file_name = 'twin' + current_time + file_extension
        return os.path.join(folder_finish, file_name)

    def make_html(key_list):
        name_f = full_path_name_file('.html')
        html = ET.Element('html')
        body = ET.Element('body')
        html.append(body)
        table = ET.Element('table')
        body.append(table)
        for line in key_list:
            tr = ET.Element('tr')
            table.append(tr)
            td = ET.Element('td')
            tr.append(td)
            big = ET.Element('big')
            td.append(big)
            arg = str(line)
            a = ET.Element('a', href=arg)
            a.text = str(line)
            big.append(a)
        ET.ElementTree(html).write(name_f, encoding='unicode', method='html')

    def make_txt(key_list):
        name_f = full_path_name_file('.txt')
        with open(name_f, 'a') as ouf:
            for line in key_list:
                ouf.write(line)
                ouf.write('\n')

    folder_tree(folder_start)
    meta_list.sort()

    for meta in meta_list:
        if meta_list.count(meta) > 1:
            finish_list.append(meta)

    finish_list = set(finish_list)

    for val in finish_list:
        get_key(val)

    make_html(key_list)
    make_txt(key_list)
