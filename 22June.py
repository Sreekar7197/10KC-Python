num = 0
while num < 10:
    num += 1
    if num == 8:
        break
    elif num % 2 != 0:
        continue
    print(num)