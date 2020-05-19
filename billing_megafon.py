import datetime
import time
import sys
import os
import numpy as np
import xlrd
import openpyxl

from operator import itemgetter
from tkinter import Tk, Label
from bs4 import BeautifulSoup


''' search for files to process '''
file_list = os.listdir()
link_dir = os.getcwd()
start_link = []

for link in file_list:
    start_link.append(link_dir + '\\' + link)
    a = link_dir + link
    a = a.replace('\\', '\\\\')

# Getting the right links to the files.
for link in start_link:
    if link[-5:].lower() == '.xlsx':
        excel_link = link
    elif link[-5:].lower() == '.html':
        billing_link = link


''' part of parsing the html file with billing and start creating table_finish '''
first_table = []
second_table = []

with open(billing_link) as read:
    contents = read.read()
soup = BeautifulSoup(contents, 'html.parser')


def table_parser(table_index, count_col):
    # The function parses the billing tables.  Input data are the table number in the file (index) and the number of columns in the main part.
    save_table = []
    save_table_total = ['Итого', ]
    for tag in soup.find_all('table', limit=9)[table_index]:
        for row in tag.find_all('tr')[2:-1]:
            for col in row.find_all('td'):
                save_table.append(col.text)
        arr = np.array(save_table)
        save_table = arr.reshape(-1, count_col)
        save_table = np.array(save_table).tolist()
        for row in tag.find_all('tr')[-1:]:
            for col in row.find_all('td'):
                save_table_total.append(col.text)
        save_table.append(save_table_total)
    return save_table


first_table = table_parser(6, 8)
second_table = table_parser(-1, 7)

# Added a space in the cell for formatting style.
second_table[-1].insert(1, ' ')

# Merge from two tables into one.
table_finish = np.array(np.concatenate(
    (first_table, second_table), axis=1)).tolist()

# In the last line I insert the sum of the total values of the tables (could not be paired in the pure form).
table_finish[-1].append(str(float(table_finish[-1][7]) +
                            float(table_finish[-1][-1])))

# Counting the total column (total expense for each subscriber).
for row in table_finish[:-1]:
    table_finish[table_finish.index(row)].append(
        str(round(float(row[-1]) + float(row[-8]), 2)))

# Adding three spaces to the last line for formatting style.
for row_index in range(3):
    table_finish[-1].insert(0, ' ')


''' table for page calculation table_fihish '''
unknown_nubmers = []
sheet_bd = {}
rb = xlrd.open_workbook(excel_link)
sheet = rb.sheet_by_name('БАЗА ДАННЫХ')

# Array where the item (list) is a string from the database page.
row_vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]

# Creating a dictionary key phone, meaning everything else.
for row in row_vals[1:]:
    sheet_bd[str(row[0])[:10]] = row[1:]

# Connecting the megaphone table to the exel table_finish database. And searching for unknown phone numbers.
for row in table_finish:
    if row[0].isdigit():
        if row[0] in sheet_bd:
            table_finish[table_finish.index(
                row)] = sheet_bd[row[0]][:3] + row + sheet_bd[row[0]][3:4]
        else:
            unknown_nubmers.append(row[0])

# Counting overspending and bringing in the result.
for row in table_finish[:-1]:
    if isinstance(row[-1], float):
        table_finish[table_finish.index(row)].append(
            round(float(row[-1]) - float(row[-2]), 2))
    else:
        table_finish[table_finish.index(row)].append(row[-1])


''' table for page application table_appendix '''
table_appendix = []
reserve_number_charges = []

# Downloading data from the first table (+ dictionary by phone) for use in the second sheet table.
for row in table_finish[:-1]:
    load_list = []
    load_list.extend([row[1], row[2], row[0], row[3],
                      sheet_bd[row[3]][-3], ' ', row[-2], row[-3]])
    # Searching for debtors and filling in the last two or one column + checking for "actual costs".
    if type(row[-2]) is float:
        if row[-2] >= float(row[-3]):
            load_list.append(row[-3])
        else:
            load_list.extend([row[-2], row[-1]])
    else:
        load_list.append(row[-3])
    table_appendix.append(load_list)

table_appendix = sorted(table_appendix, key=itemgetter(0))

# Numbering the sorted lines in the first field. And searching for expenses on spare phone numbers.
count = 0
for row in table_appendix:
    count += 1
    table_appendix[table_appendix.index(row)].insert(0, count)
    if ((row[2] == 'МТС') or (row[3] == 'Резерв')) and (float(row[8]) > 0):
        reserve_number_charges.append(row[4])


''' Claims for backup and unknown phone numbers '''
# It displays a warning message if one of the lists contains data that need to be clarified.
if unknown_nubmers or reserve_number_charges:
    window = Tk()
    window.title('Кажется, у кого-то проблемы...')
    lbl0 = Label(window, text='Эти номера отсутствуют в базе.',
                 font=('Calibri', 30))
    lbl0.grid(column=0, row=0)
    lbl1 = Label(window, text='\n'.join(
        unknown_nubmers), font=('Calibri', 30))
    lbl1.grid(column=0, row=1)
    lbl2 = Label(
        window, text='По этим резервным номерам идут расходы или карточка не верно заполнена.', font=('Calibri', 30))
    lbl2.grid(column=0, row=2)
    lbl3 = Label(window, text='\n'.join(
        reserve_number_charges), font=('Calibri', 30))
    lbl3.grid(column=0, row=3)
    window.mainloop()
    sys.exit(0)


''' loading table_finish and table_apendix tables into their sheets(+create sheets) '''
# Making names for new pages.
time_name = datetime.date.today()
calendar = {1: 'январь', 2: 'февраль', 3: 'март', 4: 'апрель', 5: 'май', 6: 'июнь',
            7: 'июль', 8: 'август', 9: 'сентябрь', 10: 'октябрь', 11: 'ноябрь', 12: 'декабрь'}

year = str(time_name.year)
month = time_name.month - 1
new_sheet_name_pr = 'Приложение №9 ' + calendar[month] + ' ' + year
new_sheet_name_po = 'Подсчет ' + calendar[month] + ' ' + year

wb = openpyxl.load_workbook(excel_link, read_only=False)


def copy_sheets(name_sheet):
    # Copied the sheets.
    sourece = wb[name_sheet]
    wb.copy_worksheet(sourece)


copy_sheets('_подсчет_месяц_год')
copy_sheets('_приложение_месяц_год')


def finish_sheet(table_name, copy_name, start_row_index, start_col_index, new_sheet_name):
    # Renamed the copied sheets + filled them with data.
    sheet = wb[copy_name]
    row_index = start_row_index
    for row in table_name:
        row_index += 1
        col_index = start_col_index
        for col in row:
            col_index += 1
            col = str(col)
            col = col.replace('.', ',')
            value = col
            cell = sheet.cell(row=row_index, column=col_index)
            cell.value = value
    sheet.title = new_sheet_name


finish_sheet(table_finish, '_подсчет_месяц_год Copy', 2, 1, new_sheet_name_po)
finish_sheet(table_appendix, '_приложение_месяц_год Copy',
             19, 0, new_sheet_name_pr)

wb.save(excel_link)

# Conclusion of a successful execution message.
window = Tk()
window.title('Успешное выполнение!!!')
lbl = Label(window, text='Биллинг успешно посчитан, просто закройте окно.',
            font=('Calibri', 30))
lbl.grid(column=0, row=0)
window.mainloop()
