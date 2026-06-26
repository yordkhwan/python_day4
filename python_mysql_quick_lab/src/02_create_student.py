"""02: Create a new student record."""

from mysql.connector import Error

from db_config import get_connection


def create_student(student_code: str, full_name: str, department: str, email: str, gpa: float) -> None:
    sql = """
        INSERT INTO students (student_code, full_name, department, email, gpa)
        VALUES (%s, %s, %s, %s, %s)
    """
    values = (student_code, full_name, department, email, gpa)

    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(sql, values)
        connection.commit()
        print(f"เพิ่มข้อมูลนักศึกษาเรียบร้อย: {full_name}")
        print("ID ใหม่:", cursor.lastrowid)
    except Error as error:
        connection.rollback()
        print("เพิ่มข้อมูลไม่สำเร็จ")
        print("Error:", error)
    finally:
        cursor.close()
        connection.close()


def main() -> None:
    create_student(
        student_code="STD006",
        full_name="Pimchanok Python",
        department="Digital Business Technology",
        email="pimchanok@example.com",
        gpa=3.45,
    )


if __name__ == "__main__":
    main()
