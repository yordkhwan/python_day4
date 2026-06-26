from datetime import date, time, datetime

today = date.today()
meeting_time = time(9, 30)
created_at = datetime.now()

print(today)
print(meeting_time)
print(created_at)
print(created_at.year)
print(created_at.month)
print(created_at.day)