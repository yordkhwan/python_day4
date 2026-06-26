# ไม่แนะนำ
def demo_not_recommended():
    try:
        result = 10 / value
        print(result)

    except:
        print("เกิดข้อผิดพลาด")


# แนะนำมากกว่า
def demo_recommended():
    try:
        result = 10 / value
        print(result)

    except ZeroDivisionError:
        print("ตัวหารต้องไม่เป็นศูนย์")

    except NameError:
        print("ยังไม่ได้ประกาศตัวแปร value")


def main():
    print("=== Do Not Recommend ===")
    demo_not_recommended()

    print("\n=== Recommend ===")
    demo_recommended()


if __name__ == "__main__":
    main()