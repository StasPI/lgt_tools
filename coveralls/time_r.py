import datetime
import calendar

# срок эксплуатации из бд присвоенный для каждого предмета
srok = 24

def generator_end_date(sourcedate, months):
    # геерит дату окончания срока эксплуатации путем добавляения во время прислоения к текущей
    # дате + срока эксплуатации
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year, month)[1])
    return datetime.date(year, month, day)


# дата передачи в эксплуатацию для фиксации в бд во время присвоения
start_date = datetime.date.today()
print(start_date)

# дата окончания срока эксплуатации для фииксации в бд во время присвоения
end_date= generator_end_date(start_date, srok)
print(end_date)

# условно строковое значение полученное из бд
from_db = '2022-07-12'

# вычисление оставшегося срока в днях
b = datetime.datetime.strptime(from_db, '%Y-%m-%d').date()
days_left = b - start_date
print(days_left)


