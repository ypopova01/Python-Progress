import datetime

current_day = datetime.datetime.now().today()
next_bday = datetime.datetime.strptime("02.07.2019", "%d.%m.%Y")
days_until_next_bday = next_bday - current_day
print(days_until_next_bday.days)