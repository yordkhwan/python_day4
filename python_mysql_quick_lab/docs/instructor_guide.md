# คู่มือสอน Python + MySQL Quick Lab

## ระยะเวลาแนะนำ

ประมาณ 90–120 นาที

## วัตถุประสงค์

ให้ผู้เรียนเข้าใจการเชื่อมต่อ Python กับ MySQL และสามารถเขียนโปรแกรม CRUD พื้นฐานได้จริง

## เครื่องมือที่ต้องใช้

- Python 3.10 ขึ้นไป
- MySQL Server หรือ XAMPP/MariaDB
- VS Code
- MySQL Workbench, phpMyAdmin หรือ command line

## แผนการสอนแบบ Step-by-step

### ช่วงที่ 1: อธิบายภาพรวม 10 นาที

อธิบายว่า Python ไม่ได้เก็บข้อมูลถาวรเองในตัวโปรแกรม แต่สามารถเชื่อมต่อฐานข้อมูล เช่น MySQL เพื่อบันทึก ค้นหา แก้ไข และลบข้อมูลได้

โครงสร้างแนวคิด:

```text
Python Program → MySQL Connector → MySQL Database → Table students
```

### ช่วงที่ 2: สร้างฐานข้อมูล 15 นาที

ให้ผู้เรียนรัน SQL ตามลำดับ:

1. `01_create_database.sql`
2. `02_create_tables.sql`
3. `03_insert_sample_data.sql`
4. `04_test_queries.sql`

จุดเน้น:

- `CREATE DATABASE`
- `CREATE TABLE`
- `INSERT INTO`
- `SELECT`

### ช่วงที่ 3: ติดตั้ง Library 10 นาที

```bash
pip install -r requirements.txt
```

อธิบาย package หลัก:

- `mysql-connector-python` ใช้เชื่อมต่อ MySQL
- `python-dotenv` ใช้อ่านค่าจากไฟล์ `.env`

### ช่วงที่ 4: ทดสอบการเชื่อมต่อ 10 นาที

รัน:

```bash
python src/01_test_connection.py
```

หาก Error ให้ตรวจสอบ:

- MySQL เปิดอยู่หรือไม่
- host/port ถูกต้องหรือไม่
- user/password ถูกต้องหรือไม่
- สร้าง database แล้วหรือยัง

### ช่วงที่ 5: CRUD ทีละขั้น 40 นาที

| ไฟล์ | แนวคิด |
|---|---|
| `02_create_student.py` | INSERT เพิ่มข้อมูล |
| `03_read_students.py` | SELECT อ่านข้อมูล |
| `04_update_student.py` | UPDATE แก้ไขข้อมูล |
| `05_delete_student.py` | DELETE ลบข้อมูล |
| `06_crud_menu.py` | รวม CRUD เป็นเมนู |

จุดที่ควรย้ำ:

- ใช้ `%s` แทนการต่อ string SQL เอง
- หลัง INSERT/UPDATE/DELETE ต้องใช้ `connection.commit()`
- ใช้ `rollback()` เมื่อเกิด Error
- ปิด cursor และ connection ทุกครั้ง

### ช่วงที่ 6: Mini Challenge 20 นาที

ให้ผู้เรียนปรับโปรแกรมเพิ่มความสามารถต่อไปนี้:

1. ค้นหานักศึกษาจาก GPA ขั้นต่ำ
2. เพิ่มเมนูค้นหาด้วยรหัสนักศึกษา
3. เพิ่ม field เบอร์โทรศัพท์ในตาราง
4. Export เฉพาะนักศึกษาที่ GPA มากกว่า 3.00

## คำถามท้าย Lab

1. ทำไมต้องใช้ `commit()` หลัง INSERT/UPDATE/DELETE?
2. `cursor(dictionary=True)` ต่างจาก cursor ปกติอย่างไร?
3. ทำไมไม่ควรเขียน SQL แบบนำ input มาต่อ string โดยตรง?
4. ถ้าเชื่อมต่อฐานข้อมูลไม่ได้ ควรตรวจสอบอะไรบ้าง?
5. ถ้าต้องนำระบบนี้ไปใช้จริง ควรเพิ่มเรื่องใดบ้าง?

## แนวทางประยุกต์ใช้ในงานจริง

- ระบบทะเบียนผู้เรียนขนาดเล็ก
- ระบบบันทึกครุภัณฑ์
- ระบบบันทึกการยืมคืนอุปกรณ์
- ระบบรายชื่อผู้เข้าอบรม
- ระบบรายงานผลการเรียนหรือคะแนนกิจกรรม
