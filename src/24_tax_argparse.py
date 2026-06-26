import argparse

parser = argparse.ArgumentParser(description="คำนวณภาษีสินค้า")

parser.add_argument("price", type=float, help="ราคาสินค้า")
parser.add_argument("--tax", type=float, default=7.0, help="อัตราภาษี percent")

args = parser.parse_args()

tax_amount = args.price * args.tax / 100
total = args.price + tax_amount

print(f"ภาษี = {tax_amount:.2f}")
print(f"รวม = {total:.2f}")