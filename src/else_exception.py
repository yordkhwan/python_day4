try:
    score = float(input("คะแนน: "))

except ValueError:
    print("กรุณากรอกคะแนนเป็นตัวเลข")

else:
    if score >= 50:
        print("ผ่าน")
    else:
        print("ไม่ผ่าน")