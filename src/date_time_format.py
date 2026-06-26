from datetime import datetime

text = "21/06/2026 14:30"
value = datetime.strptime(text, "%d/%m/%Y %H:%M")

print(value)
print(value.year)
print(value.month)
print(value.day)