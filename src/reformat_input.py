from datetime import datetime

text = input("วันที่ส่งงาน (dd/mm/yyyy): ")

try:
    due_date = datetime.strptime(text, "%d/%m/%Y")

except ValueError:
    print("รูปแบบวันที่ไม่ถูกต้อง ตัวอย่าง: 21/06/2026")

else:
    print(f"บันทึกวันส่งงาน: {due_date:%Y-%m-%d}")