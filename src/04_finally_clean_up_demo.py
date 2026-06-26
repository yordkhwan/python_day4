try:
    print("เริ่มประมวลผล")
    number = int(input("ตัวเลข: "))
    print(100 / number)

except ValueError:
    print("ต้องกรอกตัวเลขเท่านั้น")

except ZeroDivisionError:
    print("ห้ามหารด้วยศูนย์")

finally:
    print("จบการทำงานของโปรแกรม")