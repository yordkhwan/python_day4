"""04: Update a student record."""

from mysql.connector import Error

from db_config import get_connection


def update_student_gpa(student_code: str, new_gpa: float) -> None:
    sql = """
        UPDATE students
        SET gpa = %s
        WHERE student_code = %s
    """

    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(sql, (new_gpa, student_code))
        connection.commit()

        if cursor.rowcount == 0:
            print("ไม่พบรหัสนักศึกษาที่ต้องการแก้ไข")
        else:
            print(f"แก้ไข GPA ของ {student_code} เป็น {new_gpa} แล้ว")
    except Error as error:
        connection.rollback()
        print("แก้ไขข้อมูลไม่สำเร็จ")
        print("Error:", error)
    finally:
        cursor.close()
        connection.close()


def main() -> None:
    update_student_gpa("STD003", 3.20)


if __name__ == "__main__":
    main()
