"""03: Read student records."""

from db_config import get_connection


def show_all_students() -> None:
    sql = """
        SELECT id, student_code, full_name, department, email, gpa
        FROM students
        ORDER BY id
    """

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(sql)
        students = cursor.fetchall()

        print("รายการนักศึกษา")
        print("-" * 80)
        for student in students:
            print(
                f"{student['id']:>2} | {student['student_code']} | "
                f"{student['full_name']} | {student['department']} | GPA {student['gpa']}"
            )
    finally:
        cursor.close()
        connection.close()


def search_by_department(department_keyword: str) -> None:
    sql = """
        SELECT id, student_code, full_name, department, gpa
        FROM students
        WHERE department LIKE %s
        ORDER BY full_name
    """

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(sql, (f"%{department_keyword}%",))
        students = cursor.fetchall()

        print(f"ผลการค้นหาแผนกที่มีคำว่า: {department_keyword}")
        for student in students:
            print(student)
    finally:
        cursor.close()
        connection.close()


def main() -> None:
    show_all_students()
    print()
    search_by_department("Digital")


if __name__ == "__main__":
    main()
