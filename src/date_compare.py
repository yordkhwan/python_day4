from datetime import date

text = input("Please enter date (YYYY-MM-DD): ")

year, month, day = map(int, text.split("-"))
today = date(year, month, day)

due_date = date(2026, 6, 25)

if due_date < today:
    status = "overdue"

elif due_date == today:
    status = "due today"

else:
    status = "upcoming"

print(f"วันนี้: {today}")
print(f"กำหนดส่ง: {due_date}")
print(f"สถานะ: {status}")