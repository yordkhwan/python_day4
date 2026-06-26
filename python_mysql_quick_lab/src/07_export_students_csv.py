"""07: Export students from MySQL to CSV."""

import csv
from pathlib import Path

from db_config import get_connection


OUTPUT_FILE = Path(__file__).resolve().parent.parent / "data" / "students_export.csv"


def export_students_to_csv() -> None:
    sql = """
        SELECT student_code, full_name, department, email, gpa, created_at
        FROM students
        ORDER BY id
    """

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()

        OUTPUT_FILE.parent.mkdir(exist_ok=True)
        with open(OUTPUT_FILE, "w", newline="", encoding="utf-8-sig") as file:
            fieldnames = ["student_code", "full_name", "department", "email", "gpa", "created_at"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

        print(f"Export สำเร็จ: {OUTPUT_FILE}")
    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    export_students_to_csv()
