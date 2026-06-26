"""06: Simple CRUD menu for classroom demonstration."""

from mysql.connector import Error

from db_config import get_connection


def list_students() -> None:
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute("SELECT id, student_code, full_name, department, gpa FROM students ORDER BY id")
        rows = cursor.fetchall()
        print("\nรายการนักศึกษา")
        print("-" * 70)
        for row in rows:
            print(f"{row['id']:>2}. {row['student_code']} | {row['full_name']} | {row['department']} | GPA {row['gpa']}")
    finally:
        cursor.close()
        connection.close()


def add_student() -> None:
    student_code = input("รหัสนักศึกษา: ").strip()
    full_name = input("ชื่อ-สกุล: ").strip()
    department = input("แผนก/สาขา: ").strip()
    email = input("Email: ").strip()
    gpa = float(input("GPA: ").strip())

    sql = """
        INSERT INTO students (student_code, full_name, department, email, gpa)
        VALUES (%s, %s, %s, %s, %s)
    """

    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(sql, (student_code, full_name, department, email, gpa))
        connection.commit()
        print("เพิ่มข้อมูลเรียบร้อย")
    except Error as error:
        connection.rollback()
        print("เพิ่มข้อมูลไม่สำเร็จ:", error)
    finally:
        cursor.close()
        connection.close()


def edit_gpa() -> None:
    student_code = input("รหัสนักศึกษาที่ต้องการแก้ GPA: ").strip()
    new_gpa = float(input("GPA ใหม่: ").strip())

    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("UPDATE students SET gpa = %s WHERE student_code = %s", (new_gpa, student_code))
        connection.commit()
        print("แก้ไขข้อมูลเรียบร้อย" if cursor.rowcount else "ไม่พบข้อมูล")
    except Error as error:
        connection.rollback()
        print("แก้ไขข้อมูลไม่สำเร็จ:", error)
    finally:
        cursor.close()
        connection.close()


def remove_student() -> None:
    student_code = input("รหัสนักศึกษาที่ต้องการลบ: ").strip()
    confirm = input(f"ยืนยันลบ {student_code}? พิมพ์ YES เพื่อยืนยัน: ").strip()

    if confirm != "YES":
        print("ยกเลิกการลบ")
        return

    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM students WHERE student_code = %s", (student_code,))
        connection.commit()
        print("ลบข้อมูลเรียบร้อย" if cursor.rowcount else "ไม่พบข้อมูล")
    except Error as error:
        connection.rollback()
        print("ลบข้อมูลไม่สำเร็จ:", error)
    finally:
        cursor.close()
        connection.close()


def main() -> None:
    while True:
        print("\n=== Python + MySQL CRUD Menu ===")
        print("1. แสดงรายการนักศึกษา")
        print("2. เพิ่มนักศึกษา")
        print("3. แก้ไข GPA")
        print("4. ลบนักศึกษา")
        print("0. ออกจากโปรแกรม")

        choice = input("เลือกเมนู: ").strip()

        if choice == "1":
            list_students()
        elif choice == "2":
            add_student()
        elif choice == "3":
            edit_gpa()
        elif choice == "4":
            remove_student()
        elif choice == "0":
            print("จบการทำงาน")
            break
        else:
            print("กรุณาเลือกเมนูให้ถูกต้อง")


if __name__ == "__main__":
    main()
