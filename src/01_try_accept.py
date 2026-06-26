try:
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))
    
    total = price * quantity
    
    print(f"Total = {total:.2f}")

except ValueError:
    print("Please re-enter valid numbers.")