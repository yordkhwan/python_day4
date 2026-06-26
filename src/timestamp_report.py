from datetime import datetime

now = datetime.now()
report_name = now.strftime("report_%Y%m%d_%H%M%S.txt")

print(f"สร้างรายงานเมื่อ: {now}")
print(f"ชื่อไฟล์รายงาน: {report_name}")