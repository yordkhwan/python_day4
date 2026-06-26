# Python + MySQL Quick Lab

ชุดไฟล์สำหรับสอนแบบเร่งรัดเรื่องการเชื่อมต่อ Python กับ MySQL และการทำ CRUD

## เป้าหมายการเรียนรู้

เมื่อทำ Lab นี้จบ ผู้เรียนจะสามารถ:

1. สร้างฐานข้อมูลและตารางใน MySQL ได้
2. เชื่อมต่อ MySQL ด้วย Python ได้
3. เขียนคำสั่ง CRUD: Create, Read, Update, Delete ได้
4. ใช้ parameterized query เพื่อลดความเสี่ยง SQL Injection ได้
5. แยกไฟล์ config และไฟล์ logic ให้เป็นระเบียบเบื้องต้นได้

## โครงสร้างไฟล์

```text
python_mysql_quick_lab/
├── README.md
├── requirements.txt
├── .env.example
├── sql/
│   ├── 01_create_database.sql
│   ├── 02_create_tables.sql
│   ├── 03_insert_sample_data.sql
│   └── 04_test_queries.sql
├── src/
│   ├── db_config.py
│   ├── 01_test_connection.py
│   ├── 02_create_student.py
│   ├── 03_read_students.py
│   ├── 04_update_student.py
│   ├── 05_delete_student.py
│   ├── 06_crud_menu.py
│   └── 07_export_students_csv.py
├── data/
│   └── students_export_sample.csv
└── docs/
    └── instructor_guide.md
```

## การติดตั้งเครื่องมือ

### 1) ติดตั้ง Python Package

```bash
pip install -r requirements.txt
```

### 2) สร้างไฟล์ .env

คัดลอกไฟล์ `.env.example` เป็น `.env`

```bash
cp .env.example .env
```

บน Windows ใช้คำสั่ง:

```cmd
copy .env.example .env
```

จากนั้นแก้ไขค่าให้ตรงกับเครื่องของผู้เรียน เช่น username/password ของ MySQL

### 3) สร้างฐานข้อมูล

เปิด MySQL Workbench, phpMyAdmin หรือ command line แล้วรันไฟล์ SQL ตามลำดับ:

1. `sql/01_create_database.sql`
2. `sql/02_create_tables.sql`
3. `sql/03_insert_sample_data.sql`
4. `sql/04_test_queries.sql` เพื่อทดสอบข้อมูล

## ลำดับการสอนที่แนะนำ

1. อธิบายภาพรวม Python → Connector → MySQL
2. รัน SQL สร้างฐานข้อมูล
3. ติดตั้ง package ด้วย `pip install -r requirements.txt`
4. ทดสอบเชื่อมต่อด้วย `src/01_test_connection.py`
5. สอน CRUD ทีละไฟล์ ตั้งแต่ Create ถึง Delete
6. ปิดท้ายด้วยเมนูรวม `src/06_crud_menu.py`
7. เสริม Export CSV ด้วย `src/07_export_students_csv.py`

## คำสั่งรันตัวอย่าง

```bash
python src/01_test_connection.py
python src/02_create_student.py
python src/03_read_students.py
python src/04_update_student.py
python src/05_delete_student.py
python src/06_crud_menu.py
python src/07_export_students_csv.py
```

## หมายเหตุเพื่อความปลอดภัย

ตัวอย่างนี้ใช้ parameterized query เช่น `%s` และส่งค่าแยกผ่าน tuple เพื่อหลีกเลี่ยงการนำข้อความจากผู้ใช้ไปต่อกับ SQL โดยตรง ซึ่งช่วยลดความเสี่ยง SQL Injection
