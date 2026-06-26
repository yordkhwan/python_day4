"""05: Delete a student record."""

from mysql.connector import Error

from db_config import get_connection


def delete_student(student_code: str) -> None:
    sql = "DELETE FROM students WHERE student_code = %s"

    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(sql, (student_code,))
        connection.commit()

        if cursor.rowcount == 0:
            print("ไม่พบรหัสนักศึกษาที่ต้องการลบ")
        else:
            print(f"ลบข้อมูลนักศึกษา {student_code} แล้ว")
    except Error as error:
        connection.rollback()
        print("ลบข้อมูลไม่สำเร็จ")
        print("Error:", error)
    finally:
        cursor.close()
        connection.close()


def main() -> None:
    # ใช้ STD006 เพื่อทดสอบ เพราะเป็นข้อมูลที่เพิ่มจากไฟล์ 02_create_student.py
    delete_student("STD006")


if __name__ == "__main__":
    main()
