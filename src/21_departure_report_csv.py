from csv import DictReader
from datetime import datetime
from pathlib import Path

DATE_FORMAT = "%d/%m/%Y %H:%M"
BASE_DIR = Path(__file__).resolve().parent.parent
CSV_FILE = BASE_DIR / "data" / "trips.csv"


def read_trips(csv_file):
    """อ่านข้อมูลเที่ยวเดินทางจากไฟล์ CSV แล้วคืนค่าเป็น list ของ dict"""
    with open(csv_file, "r", encoding="utf-8-sig", newline="") as file:
        reader = DictReader(file)
        return list(reader)


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
    early_count = 0
    on_time_count = 0
    invalid_count = 0

    try:
        trips = read_trips(CSV_FILE)
    except FileNotFoundError:
        print(f"ไม่พบไฟล์ข้อมูล: {CSV_FILE.name}")
        return

    for trip in trips:
        try:
            trip_id = trip["id"]
            status, minutes = get_trip_status(trip["plan"], trip["actual"])
        except KeyError as error:
            print(f"ไฟล์ CSV ไม่มีคอลัมน์ที่ต้องใช้: {error}")
            return
        except ValueError:
            print(f"{trip.get('id', 'unknown')}: รูปแบบเวลาไม่ถูกต้อง")
            invalid_count += 1
            continue

        if status == "delayed":
            delayed_count += 1
        elif status == "early":
            early_count += 1
        else:
            on_time_count += 1

        print(f"{trip_id}: {status} ({minutes} นาที)")

    print("-" * 30)
    print(f"จำนวนเที่ยวที่ล่าช้า: {delayed_count}")
    print(f"จำนวนเที่ยวที่ออกก่อนเวลา: {early_count}")
    print(f"จำนวนเที่ยวที่ตรงเวลา: {on_time_count}")
    print(f"จำนวนเที่ยวที่ข้อมูลผิดรูปแบบ: {invalid_count}")


if __name__ == "__main__":
    main()
