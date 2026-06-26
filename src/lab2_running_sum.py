total = 0.0
count = 0

while True:
    text = input("กรอกตัวเลข หรือ q เพื่อจบ: ")

    if text.lower() == "q":
        break

    try:
        number = float(text)
        total += number
        count += 1

    except ValueError:
        print("กรุณากรอกตัวเลขที่ถูกต้อง")

print("จบโปรแกรม")
print(f"จำนวนข้อมูล = {count}")
print(f"ผลรวม = {total:.2f}")

if count >0:
    print(f"average={total/count:.2f}")