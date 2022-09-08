from datetime import datetime, date
import pytz
import calendar
import locale
locale.setlocale(locale.LC_ALL, 'es_ES')

tz_BA = pytz.timezone('America/Argentina/Buenos_Aires')
date_BA = datetime.now(tz_BA).strftime("%d/%m/%y")


tz_BA = pytz.timezone('America/Argentina/Buenos_Aires')
time_BA = datetime.now(tz_BA).strftime("%H:%M:%S")


my_date = date.today()
day_name_BA = calendar.day_name[my_date.weekday()]


bloque = day_name_BA[0].upper() + day_name_BA[1].upper()

if time_BA > '07:45:00' and time_BA < '09:05:00': 
    bloque += '1'
elif time_BA > '09:06:00' and time_BA < '10:40:00': 
    bloque += '2'
elif time_BA > '10:41:00' and time_BA < '12:15:00': 
    bloque += '3'
elif time_BA > '12:16:00' and time_BA < '14:30:00': 
    bloque += '4'
elif time_BA > '14:31:00' and time_BA < '16:00:00': 
    bloque += '5'
elif time_BA > '16:01:00' and time_BA < '17:30:00': 
    bloque += '6'


print(bloque)
print(time_BA)