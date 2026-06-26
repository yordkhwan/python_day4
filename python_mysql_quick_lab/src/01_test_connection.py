"""01: Test MySQL connection."""

from mysql.connector import Error

from db_config import get_connection


def main() -> None:
    try:
        connection = get_connection()
        if connection.is_connected():
            print("เชื่อมต่อ MySQL สำเร็จ")
            print("Database:", connection.database)
    except Error as error:
        print("เชื่อมต่อ MySQL ไม่สำเร็จ")
        print("Error:", error)
    finally:
        if "connection" in locals() and connection.is_connected():
            connection.close()
            print("ปิดการเชื่อมต่อแล้ว")


if __name__ == "__main__":
    main()
