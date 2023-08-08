import datetime
import time
from datetime import date, timedelta

# current_date = time.strftime("%Y %d %B %A, %H; %M; %S")
now = datetime.datetime.now()

current_date = time.strftime("%Y %d %B %A")

current_time = time.strftime("%H:%M")

one_day = timedelta(days=0, hours=8, minutes=0)
two_days = timedelta(days=1, hours=10, minutes=30)
arrive_time = timedelta(hours=15)

tomorrow = now + one_day

tomorrow_time = tomorrow.strftime("%H:%M")

arrive_day = now + two_days

arrive_time = arrive_day.strftime("%H:%M")

print(f"Сьогодні {current_date, current_time} . Завтра о {tomorrow_time} я їду за місто. Повертаюсь через день {arrive_day, arrive_time}")

print(now.today())