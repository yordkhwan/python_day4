-- 03_insert_sample_data.sql
-- เพิ่มข้อมูลตัวอย่างสำหรับใช้สอน Read / Update / Delete

USE python_quick_lab;

INSERT INTO students (student_code, full_name, department, email, gpa) VALUES
('STD001', 'Anan Chaiya', 'Digital Business Technology', 'anan@example.com', 3.25),
('STD002', 'Malee Suksan', 'Accounting', 'malee@example.com', 3.65),
('STD003', 'Krit Phatthalung', 'Electrical Power', 'krit@example.com', 2.95),
('STD004', 'Suda Surat', 'Marketing', 'suda@example.com', 3.80),
('STD005', 'Narin Tech', 'Mechatronics and Robotics', 'narin@example.com', 3.10);
