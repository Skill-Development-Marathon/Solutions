def isSameAfterReversals(num: int) -> bool:
    reversed1 = 0
    a = num
    while (num > 0):

        remainder = num % 10
        reversed1 = (reversed1 * 10) + remainder
        num = num // 10

    reversed2 = 0
    while (reversed1 > 0):
        remainder = reversed1 % 10
        reversed2 = (reversed2 * 10) + remainder
        reversed1 = reversed1 // 10

    if a == reversed2:
        return True
    else:
        return False

print(isSameAfterReversals(123))