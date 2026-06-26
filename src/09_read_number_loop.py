def read_number(prompt):
    while True:
        try:
            return float(input(prompt))

        except ValueError:
            print("กรุณากรอกตัวเลขใหม่อีกครั้ง")


price = read_number("ราคาสินค้า: ")
quantity = read_number("จำนวน: ")

print(f"ยอดรวม = {price * quantity:.2f}")