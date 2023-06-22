def count_num(num):
    count = 0
    li = [i for i in str(num)]
    
    for i in li:
        if num % int(i) == 0:
            count += 1
    return count