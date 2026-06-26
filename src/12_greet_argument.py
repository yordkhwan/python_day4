# save as greet.py
import sys

print(sys.argv)

if len(sys.argv) < 2:
    print("วิธีใช้: python greet.py <name>")
    sys.exit(1)

name = sys.argv[1]
print(f"สวัสดี {name}")