import datetime
import time
from datetime import date, timedelta

# current_date = time.strftime("%Y %d %B %A, %H; %M; %S")
now = date.today()

current_date = time.strftime("%Y %d %B %A")

current_time = time.strftime("%H:%M")

one_day = timedelta(days=1, hours=12, minutes=30)
two_days = timedelta(days=2, hours=17, minutes=00)

tomorrow = now + one_day

tomorrow_time = tomorrow.strftime("%H:%M")

arrive_day = now + two_days

arrive_time = arrive_day.strftime("%H:%M")

print(f"Сьогодні {current_date, current_time} . Завтра о {tomorrow_time} я їду за місто. Повертаюсь через день {arrive_day, arrive_time}")