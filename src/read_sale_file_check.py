filename = "data/sales.txt"

try:
    with open(filename, "r", encoding="utf-8") as file:
        value = float(file.read().strip())
        print(f"ยอดขาย = {value:,.2f}")

except FileNotFoundError:
    print(f"ไม่พบไฟล์ {filename}")

except ValueError:
    print("ข้อมูลในไฟล์ไม่ใช่ตัวเลข")

except PermissionError:
    print("ไม่มีสิทธิ์อ่านไฟล์นี้")