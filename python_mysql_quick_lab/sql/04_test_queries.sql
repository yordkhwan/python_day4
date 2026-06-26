-- 04_test_queries.sql
-- คำสั่ง SQL สำหรับตรวจสอบข้อมูลเบื้องต้น

USE python_quick_lab;

SELECT * FROM students;

SELECT id, student_code, full_name, department, gpa
FROM students
WHERE gpa >= 3.00
ORDER BY gpa DESC;

SELECT department, COUNT(*) AS total_students
FROM students
GROUP BY department;
