import time

print("เริ่มทำงาน")
time.sleep(1)
print("ผ่านไปประมาณ 1 วินาที")

start = time.perf_counter()

for number in range(1_000_000):
    pass

end = time.perf_counter()

print(f"ใช้เวลา {end - start:.6f} วินาที")