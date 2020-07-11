import subprocess
import calendar
import datetime
import os
import shutil
import psycopg2
import sys

sd_path = r'\\support-omts...'
temp_path = r'\\OB\ОМТС\!ВОДА\temp'
report_path = r'U:\ОМТС\!ВОДА\Отчет по воде.xlsx'
application_mounths = []
application_number_mounths = dict()
path_months = []
final = dict()

def error_message(error_text):
    from tkinter import Tk, Label
    window = Tk()
    window.title('Кажется, у кого-то проблемы...')
    lbl0 = Label(window, text=error_text,
                font=('Calibri', 30))
    lbl0.grid(column=0, row=0)
    window.mainloop()
    sys.exit(0)


def clean(temp_path):
    all_file_dir = os.listdir(temp_path)
    for file in all_file_dir:
        full_path = os.path.join(temp_path, file)
        os.remove(full_path)


# File pre-cleaning
clean(temp_path)
'''
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
receiving data from the database for the last 3 months, sql db
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''

now_date = datetime.datetime.now()
nubmer_days_ago = now_date - datetime.timedelta(days=90)


def mod_bigint_time(mod_t):
    # Date modification in bigint
    mod_t = datetime.datetime.timestamp(mod_t)
    return str(int(mod_t)) + '000'


ago = mod_bigint_time(nubmer_days_ago)
now = mod_bigint_time(now_date)
try:
    connection = psycopg2.connect(user="",
                                password="",
                                host="",
                                port="",
                                database="")
except:
    error_message('Нет соединения с базой данных')    

cursor = connection.cursor()
cursor.execute(f"""SELECT 
    wo.WORKORDERID  as "ID заявки"
    ,wo.TITLE as "Тема" 
    FROM WorkOrder wo 
    LEFT JOIN WorkOrderStates as wos  ON wo.WORKORDERID = wos.WORKORDERID 
    LEFT JOIN StatusDefinition as std  ON wos.STATUSID = std.STATUSID 
    LEFT JOIN WorkOrder_Queue as woq  ON wo.WORKORDERID = woq.WORKORDERID 
    WHERE std.STATUSNAME = 'Open' 
    AND wo.CREATEDTIME > bigint '{ago}'
    AND wo.CREATEDTIME != 0 
    AND wo.CREATEDTIME IS NOT NULL
    AND wo.CREATEDTIME <= bigint '{now}'  
    AND wo.CREATEDTIME != 0 
    AND wo.CREATEDTIME IS NOT NULL 
    AND wo.CREATEDTIME != -1
    AND ( woq.QUEUEID IN (4,301) OR wos.OWNERID = 819 OR wo.REQUESTERID = 819)
    AND wo.ISPARENT='1'
    """)

db_data = cursor.fetchall()
cursor.close()
connection.close()


def find_month(application_name):
    # Search for matching tickets by checkword and retrieve a month
    try:
        application_name = application_name.split()
        if application_name[0] == 'ВОДА.':
            return application_name[1][:-1]
    except:
        pass


for row in db_data:
    # Collection of months and a dictionary with the key number and
    # the month value
    month = find_month(row[1])
    if month:
        application_mounths.append(month)
        application_number_mounths[row[0]] = month

application_mounths = set(application_mounths)
'''
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
creation of a part of path to limit the search to 3 months, sd folder
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''


def generator_of_months(sourcedate, months):
    # The creation of a time-like display system minus the required
    # period in increments of a month
    month = sourcedate.month - 1 - months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year, month)[1])
    return datetime.date(year, month, day).strftime('%b%Y')


somedate = datetime.date.today()
control_months = (generator_of_months(somedate,
                                      0), generator_of_months(somedate, 1),
                  generator_of_months(somedate, 2))

# Creating a path to the folders in which you want to search
for month in control_months:
    path_month = os.path.join(sd_path, month)
    path_months.append(path_month)
'''
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
create a dictionary with paths to the desired application files
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''


def check_extension(base_name):
    # Check for compliance with the desired format
    extension = '.xlsx'
    file_name, file_extension = os.path.splitext(base_name)
    if file_extension == extension:
        return True


def find_file(path_application):
    # Listing files in a folder and submitting them for compliance verification
    tree_application = os.walk(path_application)
    for tree in tree_application:
        for file in tree[2]:
            full_path = os.path.join(tree[0], file)
            base_name = os.path.basename(file)
            if check_extension(base_name):
                list_of_applications.append(full_path)


def folder_application(path_month, key):
    # Search in the folder of the month for a suitable application number and,
    # if so, go to the application folder
    tree = os.walk(path_month)
    for folder in tree:
        if key in folder[1]:
            path_application = os.path.join(path_month, key)
            find_file(path_application)


def folder_month(key):
    # Listing of places by month where to look for applications
    for path_month in path_months:
        folder_application(path_month, key)


# Listing of months in which there are current applications
for month in application_mounths:
    list_of_applications = []
    for key, value in application_number_mounths.items():
        if month == value:
            folder_month(str(key))
    final[month] = list_of_applications
'''
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
selection and copying of applications to the report generation folder
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''


def copy_past(full_path_month, file_month_list):
    # Copies files to the folder where the report takes data
    # Adds a stamp to files with the same name to save all files
    count = 0
    for file_link in file_month_list:
        base_name = os.path.basename(file_link)
        if base_name not in os.listdir(full_path_month):
            shutil.copy2(file_link, full_path_month, follow_symlinks=True)
        else:
            file_name, file_extension = os.path.splitext(base_name)
            full_path_new_file = os.path.join(
                full_path_month, (file_name + str(count) + file_extension))
            shutil.copy2(file_link, full_path_new_file, follow_symlinks=True)
            count += 1


# Where more applications that month for the report we consider relevant
application_mounths = list(application_mounths)
if len(application_mounths) > 2:
    error_message('Слишком много не закрытых заявок! Закройте старые заявки.')
elif len(application_mounths) == 2:
    if len(final[application_mounths[0]]) > len(final[application_mounths[1]]):
        copy_past(temp_path, final[application_mounths[0]])
    else:
        copy_past(temp_path, final[application_mounths[1]])
elif len(application_mounths) == 1:
    copy_past(temp_path, final[application_mounths[0]])
else:
    error_message('Заявок найдено не было...')
'''
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
run a report in which you need to update data
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''

subprocess.Popen(report_path, shell=True)
