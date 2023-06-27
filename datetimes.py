import datetime

today = datetime.date.today()
bday = datetime.date(2023, 12, 12)

# tdelta = datetime.timedelta(days=7)
# print(today + tdelta)
till_bday = bday - today

print(f'today is: {today}')
print(f'birthday at: {today}')
print(f'birthday after: {till_bday}')

print(datetime.datetime.today()) # not time zoneaware

# for timezone aware datetimes, intall pytz

# print(datetime.datetime.now(tz=pytz.UTC))
# print(datetime.datetime.now(tz=pytz.timezone('US/Mountain')).strftime('%B %d, %Y'))