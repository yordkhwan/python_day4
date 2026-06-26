from datetime import datetime, timedelta

start_date = datetime(2026, 6, 21, 9, 0)
duration = timedelta(days=3, hours=2)
deadline = start_date + duration

print(f"เริ่ม: {start_date}")
print(f"ครบกำหนด: {deadline}")
print(f"เหลืออีก: {deadline - datetime.now()}")