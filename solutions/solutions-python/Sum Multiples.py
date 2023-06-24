def sss(num):
    total = 0
    for i in range(1,num+1):
        if i % 3 == 0:
            total += i
        elif i % 5 == 0:
            total += i
        elif i % 7 == 0:
            total += i
    return total

print(sss(10))
print(sss(6))
print(sss(7))
print(sss(15))