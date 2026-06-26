def validate_score(score):
    if not 0 <= score <= 100:
        raise ValueError("คะแนนต้องอยู่ระหว่าง 0-100")

    return score


try:
    raw_score = input("กรอกคะแนน: ")

    score = validate_score(float(raw_score))

    if score >= 50:
        print("ผลลัพธ์: ผ่าน")
    else:
        print("ผลลัพธ์: ไม่ผ่าน")

except ValueError as error:
    print(f"ข้อมูลไม่ถูกต้อง: {error}")