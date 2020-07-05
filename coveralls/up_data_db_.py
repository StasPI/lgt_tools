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
        print(command)

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