from datetime import datetime

# ข้อมูลตั้งต้นสำหรับ LAB 3
trips = [
    {"id": "A101", "plan": "21/06/2026 09:00", "actual": "21/06/2026 09:05"},
    {"id": "A102", "plan": "21/06/2026 10:30", "actual": "21/06/2026 10:25"},
    {"id": "A103", "plan": "21/06/2026 11:00", "actual": "wrong date"},
    {"id": "A104", "plan": "21/06/2026 13:00", "actual": "21/06/2026 13:00"},
    {"id": "A105", "plan": "21/08/2026 13:00", "actual": "21/06/2027 13:00"},
]

DATE_FORMAT = "%d/%m/%Y %H:%M"


# ฟังก์ชันคำนวณสถานะเวลา
def get_trip_status(plan_text, actual_text):
    plan = datetime.strptime(plan_text, DATE_FORMAT)

    actual = datetime.strptime(actual_text, DATE_FORMAT)

    diff_minutes = int((actual - plan).total_seconds() / 60)

    if diff_minutes > 0:
        return "delayed", diff_minutes

    if diff_minutes < 0:
        return "early", abs(diff_minutes)

    return "on-time", 0


def main():
    delayed_count = 0

    # วนประมวลผลข้อมูลและจัดการ Error
    for trip in trips:
        try:
            status, minutes = get_trip_status(trip["plan"], trip["actual"])

        except ValueError:
            print(f"{trip['id']}: รูปแบบเวลาไม่ถูกต้อง")
            continue

        if status == "delayed":
            delayed_count += 1

        print(f"{trip['id']}: {status} ({minutes} นาที)")

    print(f"จำนวนเที่ยวที่ล่าช้า: {delayed_count}")


if __name__ == "__main__":
    main()