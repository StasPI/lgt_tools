import psycopg2


def up_data(file, table, column):
    with open(file, 'r', encoding="utf-8") as inf:
        content = inf.read()

    all_data = content.splitlines()

    for index, value in enumerate(all_data, 0):
        value = value.split(';')
        value = list(map(lambda x: x.lstrip().strip(), value))
        all_data[index] = value

    for data in all_data:
        data = "', '".join(data)
        command = "INSERT INTO {} ({}) VALUES ('{}')".format(
            table, column, data)
        cursor.execute(command)
        connection.commit()


connection = psycopg2.connect(user="postgres",
                              password="testpass",
                              host="localhost",
                              port="5432",
                              database="testdb")

cursor = connection.cursor()

#-------------------------------------------------------------------------------------------
# file = r'clothing size.txt'
# table = 'hello_clothingsize'
# column = 'clothing_size'

# up_data(file, table, column)

#-------------------------------------------------------------------------------------------
# file = r'supplier.txt'
# table = 'hello_supplier'
# column = 'supplier'

# up_data(file, table, column)

#-------------------------------------------------------------------------------------------
# file = r'clothing.txt'
# table = 'hello_clothes'
# column = 'supplier_id, product_title, article, operational_life_in_months'

# up_data(file, table, column)

#-------------------------------------------------------------------------------------------
# file = r'data.txt'
# table = 'hello_staff'
# column = 'personnel_number, full_name, email_adress, department, job_title'

# up_data(file, table, column)

#-------------------------------------------------------------------------------------------
# file = r'.txt'
# table = 'hello_'
# column = ''

# up_data(file, table, column)

#-------------------------------------------------------------------------------------------
cursor.close()
connection.close()