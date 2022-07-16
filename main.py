import random

x = random.randint(0,128)

print(x)

st = input("答えを表示")

if (st != ""):
    print("２進数は "+bin(x))
    print("16進数は "+hex(x))
else:
    print("終了しました。")