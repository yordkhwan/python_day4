Run_ERROR_DEMO=False

def divide(a, b):
    return a / b


def main():
    x = 10
    y = 0

    print(divide(x, y))


main()

# Traceback จะบอก:
# - ไฟล์และบรรทัดที ่ error
# - call stack ว่าฟังก์ชันใดเรียกฟังก์ชันใด
# - ชนิด exception และข้อความ error