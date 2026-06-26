def calculate_discount(price, percent):
    if price < 0:
        raise ValueError("price ต้องไม่ติดลบ")

    if not 0 <= percent <= 100:
        raise ValueError("percent ต้องอยู่ระหว่าง 0-100")

    return price * percent / 100


try:
    print(calculate_discount(1000, 120))

except ValueError as error:
    print(f"ข้อมูลไม่ถูกต้อง: {error}")