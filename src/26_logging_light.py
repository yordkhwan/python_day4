def log_info(message):
    print(f"[INFO] {message}")


def log_error(message):
    print(f"[ERROR] {message}")


def main():
    log_info("เริ่มอ่านไฟล์")
    log_info("กำลังประมวลผลข้อมูล")
    log_error("ไม่พบไฟล์ input.txt")


if __name__ == "__main__":
    main()