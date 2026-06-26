from datetime import date



text=input("Please enter date YYYY-MM-DD")
year, month, day = map(int, text.split("-"))
today = date(year, month, day)
deadline = date(2026, 7, 1)
remaining_days = (deadline - today).days

if remaining_days < 0:
    print(f"เลยกำหนดแล้ว {-remaining_days} วัน")
else:
    print(f"เหลืออีก {remaining_days} วัน")