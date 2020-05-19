from tkinter import *
from tkinter import filedialog, messagebox
from tkinter import ttk
from file_sorting import start_sort
from twin_search import twin_go


def finish():
    # Completion message.
    messagebox.showinfo('All set!', 'All set!')


def start_first():
    # Starts the corresponding processing module.
    start_sort(folder_start_s, folder_finish_s)
    finish()


def start_second():
    twin_go(folder_start_t, folder_finish_t)
    finish()


def start_folder_sort():
    # Receives the selected directory by the graphic shell assignment.
    global folder_start_s
    folder_start_s = filedialog.askdirectory()
    lbl_start = Label(tab1, text=folder_start_s, font=('Arial Bold', 12))
    lbl_start.grid(column=1, row=1)


def start_folder_twin():
    global folder_start_t
    folder_start_t = filedialog.askdirectory()
    lbl_start = Label(tab2, text=folder_start_t, font=('Arial Bold', 12))
    lbl_start.grid(column=1, row=1)


def finish_folder_sort():
    # Receives the selected directory by the graphic shell assignment.
    global folder_finish_s
    folder_finish_s = filedialog.askdirectory()
    lbl_finish = Label(tab1, text=folder_finish_s, font=('Arial Bold', 12))
    lbl_finish.grid(column=1, row=2)


def finish_folder_twin():
    global folder_finish_t
    folder_finish_t = filedialog.askdirectory()
    lbl_finish = Label(tab2, text=folder_finish_t, font=('Arial Bold', 12))
    lbl_finish.grid(column=1, row=2)


def info_sort():
    # Information block.
    messagebox.showinfo(
        'Info sorting?',
        '1) The program sorts files according to the scheme "year - month", automatically determining the date of file creation; \n 2) To avoid errors before starting to use, please close all open files; \n 3) Specify to the program from which directory to take files (in case if there are subfolders in the directory, the program will scan them for files to be sorted); \n 4) Specify to the program in which directory to place the sorted directories; \n 5) Click on the button "Start!" button and wait for a pop-up window to inform you about the end of the process; \n 6) Close the program.'
    )


def info_twin():
    messagebox.showinfo(
        'Info find copies?',
        '1) The program searches for duplicate images based on name, date, size, resolution and as a result produces two files with a list of similar files; \n 2) To avoid errors before using, close all open files; \n 3) Specify to the program which directory to take files from (if there are subfolders in the directory, the program will scan them); \n 4) Specify to the program which directory to place two files with the result (it will be an html file for quick navigation through images and a txt file); \n 5) Click the button "Find copies!" and wait for a pop-up window to appear informing you that the process is over; \n 6) Close the program.'
    )


window = Tk()
window.title('Welcome to the sorter.')
window.geometry('500x130')

tab_control = ttk.Notebook(window)
# First tab.
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Sorting')
btn = Button(tab1, text='Info sorting?', command=info_sort)
btn.grid(column=0, row=0)
btn_start_folder = Button(tab1,
                          text='Grab a folder',
                          command=start_folder_sort)
btn_start_folder.grid(column=0, row=1)
btn_finish_folder = Button(tab1,
                           text='Put in a folder',
                           command=finish_folder_sort)
btn_finish_folder.grid(column=0, row=2)
btn_start_all_folder = Button(tab1, text='Start sorting!', command=start_first)
btn_start_all_folder.grid(column=0, row=3)
# Second tab.
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Find copies')
btn2 = Button(tab2, text='Info find copies?', command=info_twin)
btn2.grid(column=0, row=0)
btn2_start_folder = Button(tab2,
                           text='Grab a folder',
                           command=start_folder_twin)
btn2_start_folder.grid(column=0, row=1)
btn2_finish_folder = Button(tab2,
                            text='Put in a folder',
                            command=finish_folder_twin)
btn2_finish_folder.grid(column=0, row=2)
btn2_start_all_folder = Button(tab2, text='Find copies!', command=start_second)
btn2_start_all_folder.grid(column=0, row=3)

tab_control.pack(expand=1, fill='both')
window.mainloop()