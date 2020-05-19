'''
A preparation for creating exe files from scripts. You can use it as a standalone tool or wrap it in a function for mass conversion.
'''


import os
import shutil
import PyInstaller.__main__

exe_file_dir = r'A:\only_exe'
script_address = r'A:\git\for_lgt\doppel\gui_start.py'

PyInstaller.__main__.run([
    '--onefile',
    '--noconsole',
    '--specpath', exe_file_dir,
    '--workpath', exe_file_dir,
    '--distpath', exe_file_dir,
    script_address
])


all_file_dir = os.listdir(exe_file_dir)
for file in all_file_dir:
    file_name, file_extension = os.path.splitext(file)
    if file_extension[1:].lower() != 'exe':
        path = exe_file_dir + '\\' + file
        if os.path.isfile(path):
            os.remove(path)  # remove the file
        elif os.path.isdir(path):
            shutil.rmtree(path)  # remove dir and all contains
